from models.Test import Test

class TestSummary:
    def __init__(self, story: str) -> None:
        self.story = story
        self.test = Test()
