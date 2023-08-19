from flask import jsonify

from Service.TestStepsService import TestStepsService


class TestStepsResource:
    @classmethod
    def get(cls, _id, only_ids):
        r = TestStepsService.get(_id, only_ids)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = TestStepsService.save(body["test_id"], body["steps"])
        return jsonify({"msg": r}), 200
    
    @classmethod
    def delete(cls, _id):
        r = TestStepsService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200
