from unittest.mock import Mock

from tests.main import app, subscriber, TestEvent


def test_subscriber_registered():
    app.subscribe(TestEvent)(subscriber)

    assert TestEvent in app._event_handler.subscriptions


def test_subscriber_called():
    mock_subscriber = Mock()
    app.subscribe(TestEvent)(mock_subscriber)

    event = TestEvent()
    app._event_dispatcher(event=event)

    mock_subscriber.assert_called_with(event)
