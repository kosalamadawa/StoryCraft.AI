from flask import jsonify

from Service.ExpectService import ExpectService


class ExpectResource:
    @classmethod
    def get(cls, _id):
        r = ExpectService.get(_id)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = ExpectService.save(body["id"], body["expect"])
        return jsonify({"msg": r}), 200
    
    @classmethod
    def delete(cls, _id):
        r = ExpectService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200
