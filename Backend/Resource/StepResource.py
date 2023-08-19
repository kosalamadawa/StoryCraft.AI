from flask import jsonify

from Service.StepService import StepService


class StepResource:
    @classmethod
    def get(cls, _id):
        r = StepService.get(_id)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = StepService.save(body["id"], body["step"])
        return jsonify({"msg": r}), 200
    
    @classmethod
    def delete(cls, _id):
        r = StepService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200
