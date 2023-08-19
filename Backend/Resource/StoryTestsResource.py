from flask import jsonify

from Service.StoryTestsService import StoryTestsService


class StoryTestsResource:
    @classmethod
    def get(cls, _id, only_ids):
        r = StoryTestsService.get(_id, only_ids)
        if r == None:
            return jsonify({"msg": "not found"}), 404
        return jsonify(r), 200

    @classmethod
    def post(cls, body):
        r = StoryTestsService.save(body["story_id"], body["tests"])
        return jsonify({"msg": r}), 200
    
    @classmethod
    def delete(cls, _id):
        r = StoryTestsService.delete(_id)
        if r == 'invalid_id':
            return jsonify({'error': 'id not found'}), 404
        return jsonify({'msg': 'deleted successfully'}), 200
