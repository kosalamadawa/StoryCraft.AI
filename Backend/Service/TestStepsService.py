from DB.DB import test_steps_collection
from pymongo.errors import DuplicateKeyError

from Service.TestService import TestService
from Service.StepService import StepService


class TestStepsService:
    @classmethod
    def get(cls, _id: int, only_ids):
        r = test_steps_collection.find_one({"_id": _id})
        if r is None:
            return None
        r["test_id"] = r["_id"]
        del r["_id"]

        if only_ids:
            return r

        test = TestService.get(_id)
        if test != None:
            test = test["test"]
        steps = []

        for step in r["steps"]:
            step_res = StepService.get(step)
            if step_res != None:
                steps.append(step_res["step"])

        return {"test": test, "steps": steps}
    
    @classmethod
    def get_step_ids_by_test_id(cls, _id: int):
        r = test_steps_collection.find_one({"_id": _id})
        if r is None:
            return []
        return r["steps"]

    @classmethod
    def save(cls, test_id, steps):
        try:
            r = test_steps_collection.insert_one({"_id": test_id, "steps": steps})
            return "inserted"
        except DuplicateKeyError:
            return "duplicate_key"

    @classmethod
    def delete(cls, _id: int):
        r = test_steps_collection.delete_one({"_id": _id})
        if r.deleted_count == 0:
            return "invalid_id"
        return "ok"
