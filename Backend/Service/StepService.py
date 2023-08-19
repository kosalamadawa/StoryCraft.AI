from DB.DB import steps_collection
from pymongo.errors import DuplicateKeyError


class StepService:
    @classmethod
    def get(cls, _id: int):
        r = steps_collection.find_one({"_id": _id})
        if r is None:
            return None
        r["id"] = r["_id"]
        del r["_id"]
        return r
    
    @classmethod
    def save(cls, _id, step):
        try:
            r = steps_collection.insert_one({"_id": _id, 'step': step})
            return 'inserted'
        except DuplicateKeyError:
            return 'duplicate_key'
        
    @classmethod
    def delete(cls, _id: int):
        r = steps_collection.delete_one({'_id': _id})
        if r.deleted_count == 0:
            return 'invalid_id'
        return 'ok'