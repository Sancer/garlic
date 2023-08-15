from unittest.mock import Mock

from tests.main import app, TestEvent


def test_subscriber_registered():
    app.subscribe(TestEvent)(lambda event: None)

    assert TestEvent in app._event_handler.subscriptions


def test_subscriber_called():
    mock_subscriber = Mock()
    app.subscribe(TestEvent)(mock_subscriber)

    event = TestEvent(fizz="buzz")
    app.publish(event=event)

    mock_subscriber.assert_called_with(event)


def test_publish_and_subscriber_called():
    subscriber_mock = Mock()
    app.subscribe(TestEvent)(subscriber_mock)

    event = TestEvent(fizz="buzz")
    app.publish(event=event)

    subscriber_mock.assert_called_with(event)


def test_publish_with_two_subscribers():
    subscriber_mock = Mock()
    app.subscribe(TestEvent)(subscriber_mock)
    subscriber2_mock = Mock()
    app.subscribe(TestEvent)(subscriber2_mock)

    event = TestEvent(fizz="buzz")
    app.publish(event=event)

    subscriber_mock.assert_called_with(event)
    subscriber2_mock.assert_called_with(event)

    assert subscriber_mock.call_count == 1
    assert subscriber2_mock.call_count == 1


def test_publish_with_two_subscribers_and_two_events():
    subscriber_mock = Mock()
    app.subscribe(TestEvent)(subscriber_mock)
    subscriber2_mock = Mock()
    app.subscribe(TestEvent)(subscriber2_mock)

    event = TestEvent(fizz="buzz")
    app.publish(event=event)
    event = TestEvent(fizz="buzz")
    app.publish(event=event)

    assert subscriber_mock.call_count == 2
    assert subscriber2_mock.call_count == 2
