from DB.DB import test_expects_collection
from pymongo.errors import DuplicateKeyError

from Service.TestService import TestService
from Service.ExpectService import ExpectService


class TestExpectsService:
    @classmethod
    def get(cls, _id: int, only_ids):
        r = test_expects_collection.find_one({"_id": _id})
        if r is None:
            return None
        r["story_id"] = r["_id"]
        del r["_id"]

        if only_ids:
            return r

        test = TestService.get(_id)
        if test != None:
            test = test["test"]
        expects = []

        for expect in r["expects"]:
            expect_res = ExpectService.get(expect)
            if expect_res != None:
                expects.append(expect_res["expect"])

        return {"test": test, "expects": expects}
    
    @classmethod
    def get_expect_ids_by_test_id(cls, _id: int):
        r = test_expects_collection.find_one({"_id": _id})
        if r is None:
            return []
        return r["expects"]

    @classmethod
    def save(cls, test_id, expects):
        try:
            r = test_expects_collection.insert_one({"_id": test_id, "expects": expects})
            return "inserted"
        except DuplicateKeyError:
            return "duplicate_key"

    @classmethod
    def delete(cls, _id: int):
        r = test_expects_collection.delete_one({"_id": _id})
        if r.deleted_count == 0:
            return "invalid_id"
        return "ok"
