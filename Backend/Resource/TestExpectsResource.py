from flask import jsonify

from Service.TestExpectsService import TestExpectsService


class TestExpectsResource:
    @classmethod
    def get(cls, _id, only_ids):
        r = TestExpectsService.get(_id, only_ids)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = TestExpectsService.save(body["test_id"], body["expects"])
        return jsonify({"msg": r}), 200
    
    @classmethod
    def delete(cls, _id):
        r = TestExpectsService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200
