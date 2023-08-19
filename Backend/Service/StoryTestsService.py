from DB.DB import story_tests_collection
from pymongo.errors import DuplicateKeyError

from Service.StoryService import StoryService
from Service.TestService import TestService


class StoryTestsService:
    @classmethod
    def get(cls, _id: int, only_ids):
        r = story_tests_collection.find_one({"_id": _id})
        if r is None:
            return None
        r["story_id"] = r["_id"]
        del r["_id"]

        if only_ids:
            return r

        story = StoryService.get(_id)
        if story != None:
            story = story["story"]
        tests = []

        for test in r["tests"]:
            test_res = TestService.get(test)
            if test_res != None:
                tests.append(test_res["test"])

        return {"story": story, "tests": tests}

    @classmethod
    def get_test_ids_by_story_id(cls, _id: int):
        r = story_tests_collection.find_one({"_id": _id})
        if r is None:
            return []
        return r["tests"]

    @classmethod
    def save(cls, story_id, tests):
        try:
            r = story_tests_collection.insert_one({"_id": story_id, "tests": tests})
            return "inserted"
        except DuplicateKeyError:
            return "duplicate_key"

    @classmethod
    def delete(cls, _id: int):
        r = story_tests_collection.delete_one({"_id": _id})
        if r.deleted_count == 0:
            return "invalid_id"
        return "ok"
