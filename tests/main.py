from garlic import Garlic, BaseEvent


app = Garlic(config={})


class TestEvent(BaseEvent):
    pass


@app.subscribe(TestEvent)
def subscriber(event: TestEvent):
    pass
