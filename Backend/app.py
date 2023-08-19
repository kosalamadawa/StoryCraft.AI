import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask, request, jsonify
from flask_cors import cross_origin

from Resource.StoryResource import StoryResource
from Resource.TestResource import TestResource
from Resource.StoryTestsResource import StoryTestsResource
from Resource.StepResource import StepResource
from Resource.TestStepsResource import TestStepsResource
from Resource.ExpectResource import ExpectResource
from Resource.TestExpectsResource import TestExpectsResource
from Resource.ModelResource import ModelResource

URL_PREFIX = os.environ.get("URL_PREFIX")
API_KEY = os.environ.get("API_KEY")


app = Flask(__name__)


@app.route(URL_PREFIX + "/", methods=["GET"])
@cross_origin()
def index():
    return "Hello"


@app.route(URL_PREFIX + "/story", methods=["GET", "POST", "DELETE"])
@cross_origin()
def story():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return StoryResource.get(_id)

    if request.method == "POST":
        return StoryResource.post(request.get_json())

    if request.method == "DELETE":
        return StoryResource.delete(_id)

    return


@app.route(URL_PREFIX + "/test", methods=["GET", "POST", "DELETE"])
@cross_origin()
def test():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return TestResource.get(_id)

    if request.method == "POST":
        return TestResource.post(request.get_json())

    if request.method == "DELETE":
        return TestResource.delete(_id)

    return


@app.route(URL_PREFIX + "/story-tests", methods=["GET", "POST", "DELETE"])
@cross_origin()
def story_tests():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")
    only_ids = request.args.get("only_ids")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if only_ids is not None:
        if only_ids.strip() != "":
            if only_ids == "false" or only_ids == "False":
                only_ids = False
            elif only_ids == "true" or only_ids == "True":
                only_ids = True
            else:
                only_ids = True
        else:
            only_ids = True

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return StoryTestsResource.get(_id, only_ids)

    if request.method == "POST":
        return StoryTestsResource.post(request.get_json())

    if request.method == "DELETE":
        return StoryTestsResource.delete(_id)

    return


@app.route(URL_PREFIX + "/step", methods=["GET", "POST", "DELETE"])
@cross_origin()
def step():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return StepResource.get(_id)

    if request.method == "POST":
        return StepResource.post(request.get_json())

    if request.method == "DELETE":
        return StepResource.delete(_id)

    return


@app.route(URL_PREFIX + "/test-steps", methods=["GET", "POST", "DELETE"])
@cross_origin()
def story_steps():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")
    only_ids = request.args.get("only_ids")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if only_ids is not None:
        if only_ids.strip() != "":
            if only_ids == "false" or only_ids == "False":
                only_ids = False
            elif only_ids == "true" or only_ids == "True":
                only_ids = True
            else:
                only_ids = True
        else:
            only_ids = True

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return TestStepsResource.get(_id, only_ids)

    if request.method == "POST":
        return TestStepsResource.post(request.get_json())

    if request.method == "DELETE":
        return TestStepsResource.delete(_id)

    return


@app.route(URL_PREFIX + "/expect", methods=["GET", "POST", "DELETE"])
@cross_origin()
def expect():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return ExpectResource.get(_id)

    if request.method == "POST":
        return ExpectResource.post(request.get_json())

    if request.method == "DELETE":
        return ExpectResource.delete(_id)

    return


@app.route(URL_PREFIX + "/test-expects", methods=["GET", "POST", "DELETE"])
@cross_origin()
def story_expects():
    api_token = request.headers.get("api-key")
    _id = request.args.get("id")
    only_ids = request.args.get("only_ids")

    if _id is not None:
        if _id.strip() != "":
            try:
                _id = int(_id)
            except ValueError:
                _id = None
        else:
            _id = None

    if only_ids is not None:
        if only_ids.strip() != "":
            if only_ids == "false" or only_ids == "False":
                only_ids = False
            elif only_ids == "true" or only_ids == "True":
                only_ids = True
            else:
                only_ids = True
        else:
            only_ids = True

    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    if request.method == "GET":
        return TestExpectsResource.get(_id, only_ids)

    if request.method == "POST":
        return TestExpectsResource.post(request.get_json())

    if request.method == "DELETE":
        return TestExpectsResource.delete(_id)

    return


@app.route(URL_PREFIX + "/train", methods=["GET"])
@cross_origin()
def train():
    api_token = request.headers.get("api-key")
    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401
    model_no = request.args.get("model_no")
    if model_no is None or model_no.strip() == "":
        return jsonify({"error": "model no not found"}), 400
    return ModelResource.train(model_no)


@app.route(URL_PREFIX + "/predict", methods=["GET"])
@cross_origin()
def predict():
    api_token = request.headers.get("api-key")
    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    model_no = request.args.get("model_no")
    if model_no is None or model_no.strip() == "":
        # return jsonify({"error": "model no not found"}), 400
        model_no = ""

    text = request.args.get("text")
    if text is None:
        return jsonify({"msg": "text required"}), 400
    return ModelResource.predict(model_no, text)


@app.route(URL_PREFIX + "/reload-model", methods=["GET"])
@cross_origin()
def reload_model():
    api_token = request.headers.get("api-key")
    if api_token is None or api_token != API_KEY:
        return jsonify({"msg": "unauthorized access"}), 401

    model_no = request.args.get("model_no")
    if model_no is None or model_no.strip() == "":
        return jsonify({"error": "model no not found"}), 400
    return ModelResource.reload_model(model_no)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
