import os

import pymongo
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.environ.get("MONGO_URI")

_client = pymongo.MongoClient(MONGO_URI)
_db = _client.TrickyRailway
stories_collection = _db.Stories
tests_collection = _db.Tests
story_tests_collection = _db.StoryTests
steps_collection = _db.Steps
test_steps_collection = _db.TestSteps
expects_collection = _db.Expects
test_expects_collection = _db.TestExpects
