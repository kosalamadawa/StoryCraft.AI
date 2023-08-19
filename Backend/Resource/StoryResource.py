from flask import jsonify

from Service.StoryService import StoryService


class StoryResource:
    @classmethod
    def get(cls, _id):
        r = StoryService.get(_id)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = StoryService.save(body["id"], body["story"])
        return jsonify({"msg": r}), 200

    @classmethod
    def delete(cls, _id):
        r = StoryService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200