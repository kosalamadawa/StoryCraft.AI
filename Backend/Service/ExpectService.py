from DB.DB import expects_collection
from pymongo.errors import DuplicateKeyError


class ExpectService:
    @classmethod
    def get(cls, _id: int):
        r = expects_collection.find_one({"_id": _id})
        if r is None:
            return None
        r["id"] = r["_id"]
        del r["_id"]
        return r
    
    @classmethod
    def save(cls, _id, expect):
        try:
            r = expects_collection.insert_one({"_id": _id, 'expect': expect})
            return 'inserted'
        except DuplicateKeyError:
            return 'duplicate_key'
        
    @classmethod
    def delete(cls, _id: int):
        r = expects_collection.delete_one({'_id': _id})
        if r.deleted_count == 0:
            return 'invalid_id'
        return 'ok'