from DB.DB import stories_collection, tests_collection
from Service.TestService import TestService
from Service.StepService import StepService
from Service.ExpectService import ExpectService
from Service.StoryTestsService import StoryTestsService
from Service.TestStepsService import TestStepsService
from Service.TestExpectsService import TestExpectsService
from ml_model.train import train_model
from ml_model.inference import Inference
from flask import jsonify
from models.TestSummary import TestSummary

inference_1 = None
inference_2 = None
inference_3 = None


def get_test_summaries(testSummaries):
    summaries_data = []
    for summary in testSummaries:
        summaries_data.append(
            {
                "test": summary.test.test,
                "steps": list(map(lambda x: x["step"], summary.test.steps)),
                "expects": list(map(lambda x: x["expect"], summary.test.expects)),
            }
        )
    return summaries_data


class ModelResource:
    @classmethod
    def train(cls, model_no):
        if model_no == "1":
            rows = ""
            stories = stories_collection.find()
            for story in stories:
                row = ""
                row = row + story["story"]

                story_tests = StoryTestsService.get_test_ids_by_story_id(story["_id"])
                if len(story_tests) == 0:
                    continue
                tests = "|"
                for test in story_tests:
                    tests = tests + str(test) + ","
                row = row + tests[:-1]

                rows = rows + "\n" + row

            stories.close()

        if model_no == "2":
            rows = ""
            tests = tests_collection.find()
            for test in tests:
                row = ""
                row = row + test["test"]

                test_steps = TestStepsService.get_step_ids_by_test_id(test["_id"])
                if len(test_steps) == 0:
                    continue
                steps = "|"
                for step in test_steps:
                    steps = steps + str(step) + ","
                row = row + steps[:-1]

                rows = rows + "\n" + row

            tests.close()

        if model_no == "3":
            rows = ""
            tests = tests_collection.find()
            for test in tests:
                row = ""
                row = row + test["test"]

                test_expects = TestExpectsService.get_expect_ids_by_test_id(test["_id"])
                if len(test_expects) == 0:
                    continue
                expects = "|"
                for expect in test_expects:
                    expects = expects + str(expect) + ","
                row = row + expects[:-1]

                rows = rows + "\n" + row

            tests.close()

        with open(f"./data/dataset_{model_no}.csv", "w") as file:
            file.write(rows)

        train_model(model_no)

        return jsonify({"msg": "ok"}), 200

    @classmethod
    def predict(cls, model_no, text):
        global inference_1
        global inference_2
        global inference_3

        if model_no == "1" and inference_1 == None:
            inference_1 = Inference(model_no)
        if model_no == "2" and inference_2 == None:
            inference_2 = Inference(model_no)
        if model_no == "3" and inference_3 == None:
            inference_3 = Inference(model_no)
        else:
            inference_1 = Inference("1")
            inference_2 = Inference("2")
            inference_3 = Inference("3")

        if model_no == "":
            pred = inference_1.predict(text).toarray()[0]
            testSummaries = []
            i = 0
            for item in pred:
                if item == 0:
                    continue
                testSummaries.append(TestSummary(text))
                test = TestService.get(int(item))["test"]
                testSummaries[i].test.test = test
                pred = inference_2.predict(test).toarray()[0]
                steps = []
                for item in pred:
                    print(item)
                    if item == 0:
                        continue
                    step = StepService.get(int(item))
                    if step is not None:
                        steps.append(step)
                testSummaries[i].test.steps = steps
                pred = inference_3.predict(test).toarray()[0]
                expects = []
                for item in pred:
                    if item == 0:
                        continue
                    expect = ExpectService.get(int(item))
                    if expect is not None:
                        expects.append(expect)
                testSummaries[i].test.expects = expects
                i += 1
            return jsonify(
                {"story": text, "results": get_test_summaries(testSummaries)}
            )

        if model_no == "1":
            pred = inference_1.predict(text).toarray()[0]
            tests = []
            for item in pred:
                if item == 0:
                    continue
                test = TestService.get(int(item))
                if test is not None:
                    tests.append(test)
            return jsonify({"tests": tests}), 200

        if model_no == "2":
            pred = inference_2.predict(text).toarray()[0]
            steps = []
            for item in pred:
                if item == 0:
                    continue
                step = StepService.get(int(item))
                if step is not None:
                    steps.append(step)
            return jsonify({"steps": steps}), 200

        if model_no == "3":
            pred = inference_3.predict(text).toarray()[0]
            expects = []
            for item in pred:
                if item == 0:
                    continue
                expect = ExpectService.get(int(item))
                if expect is not None:
                    expects.append(expect)
            return jsonify({"expects": expects}), 200

    @classmethod
    def reload_model(cls, model_no):
        global inference_1
        global inference_2
        global inference_3
        if model_no == "1":
            inference_1 = Inference("1")
        elif model_no == "2":
            inference_2 = Inference("2")
        elif model_no == "3":
            inference_3 = Inference("3")
        else:
            inference_1 = Inference("1")
            inference_2 = Inference("2")
            inference_3 = Inference("3")
        return jsonify({"msg": "ok"}), 200
