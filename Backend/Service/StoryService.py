from DB.DB import stories_collection
from pymongo.errors import DuplicateKeyError


class StoryService:
    @classmethod
    def get(cls, _id: int):
        r = stories_collection.find_one({"_id": _id})
        if r is None:
            return None
        r["id"] = r["_id"]
        del r["_id"]
        return r
    
    @classmethod
    def save(cls, _id, story):
        try:
            r = stories_collection.insert_one({"_id": _id, 'story': story})
            return 'inserted'
        except DuplicateKeyError:
            return 'duplicate_key'
    
    @classmethod
    def delete(cls, _id: int):
        r = stories_collection.delete_one({'_id': _id})
        if r.deleted_count == 0:
            return 'invalid_id'
        return 'ok'