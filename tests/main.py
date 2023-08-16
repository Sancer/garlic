from garlic import Garlic, BaseEvent


app = Garlic(config={})


class TestEvent(BaseEvent):
    fizz: str
    other: str = "default"


def subscriber(event: TestEvent):
    pass



