from flask import jsonify

from Service.TestService import TestService


class TestResource:
    @classmethod
    def get(cls, _id):
        r = TestService.get(_id)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = TestService.save(body["id"], body["test"])
        return jsonify({"msg": r}), 200
    
    @classmethod
    def delete(cls, _id):
        r = TestService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200
