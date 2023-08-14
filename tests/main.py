from garlic import Garlic, BaseEvent

app = Garlic(config={})

class TestEvent(BaseEvent):
    pass


def subscriber(event: TestEvent):
    pass

