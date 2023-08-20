from unittest import mock

from tests.main import TestEvent, app, subscriber


def test_subscriber_called():
    subscriber_mock = mock.create_autospec(subscriber)
    app.subscribe()(subscriber_mock)

    event = TestEvent(fizz="buzz")
    app.emit(event=event)

    subscriber_mock.assert_called_with(event)


def test_publish_and_subscriber_called():
    subscriber_mock = mock.create_autospec(subscriber)
    app.subscribe()(subscriber_mock)

    event = TestEvent(fizz="buzz")
    app.emit(event=event)

    subscriber_mock.assert_called_with(event)


def test_publish_with_two_subscribers():
    subscriber_mock = mock.create_autospec(subscriber)
    app.subscribe()(subscriber_mock)
    subscriber2_mock = mock.create_autospec(subscriber)
    app.subscribe()(subscriber2_mock)

    event = TestEvent(fizz="buzz")
    app.emit(event=event)

    subscriber_mock.assert_called_with(event)
    subscriber2_mock.assert_called_with(event)
    assert subscriber_mock.call_count == 1
    assert subscriber2_mock.call_count == 1


def test_publish_with_two_subscribers_and_two_events():
    subscriber_mock = mock.create_autospec(subscriber)
    app.subscribe()(subscriber_mock)
    subscriber2_mock = mock.create_autospec(subscriber)
    app.subscribe()(subscriber2_mock)

    event = TestEvent(fizz="buzz")
    app.emit(event=event)
    event = TestEvent(fizz="buzz")
    app.emit(event=event)

    assert subscriber_mock.call_count == 2
    assert subscriber2_mock.call_count == 2
