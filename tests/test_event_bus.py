from unittest import mock

import pytest

from garlic import BaseEvent, EventBus
from garlic.event_bus import EventNotProvidedError
from tests.main import TestEvent


@pytest.fixture
def subscriber_mock():
    def subscriber(event: BaseEvent):
        pass

    return mock.create_autospec(subscriber)


def test_send_event_with_no_subscribers():
    event_bus = EventBus()
    event = BaseEvent()

    assert event_bus.send(event) is None


def test_send_event_to_subscriber_with_wrong_parameter_type():
    event_bus = EventBus()
    subscriber = mock.Mock()
    event = BaseEvent()

    with pytest.raises(EventNotProvidedError):
        event_bus.subscribe(subscriber)
        event_bus.send(event)


def test_get_channel_name():
    event_bus = EventBus(channel_path="path", channel_delimiter=".")

    channel_name = event_bus.get_channel_name("Event")

    assert channel_name == "path.Event"


def test_get_subscriber_event_name(subscriber_mock):
    event_bus = EventBus()

    event_name = event_bus._get_subscriber_event_name(subscriber_mock)

    assert event_name == "BaseEvent"


def test_subscription_called(subscriber_mock):
    event_bus = EventBus()
    event_bus.subscribe(subscriber=subscriber_mock)

    event = BaseEvent()
    event_bus(event=event)

    subscriber_mock.assert_called_once_with(event)


def test_subscription_called_twice_with_different_events(subscriber_mock):
    event_bus = EventBus()
    event_bus.subscribe(subscriber=subscriber_mock)
    event1 = BaseEvent()
    event_bus(event=event1)
    event2 = BaseEvent()
    event_bus(event=event1)

    subscriber_mock.assert_called_with(event1)
    subscriber_mock.assert_called_with(event2)
    assert subscriber_mock.call_count == 2


def test_two_subscriptions_called_with_different_events():
    event_bus = EventBus()

    def subscription1(event: BaseEvent):
        pass

    def subscription2(event: TestEvent):
        pass

    subscriber1_mock = mock.create_autospec(subscription1)
    subscriber2_mock = mock.create_autospec(subscription2)

    event_bus.subscribe(subscriber=subscriber1_mock)
    event_bus.subscribe(subscriber=subscriber2_mock)

    event1 = BaseEvent()
    event2 = TestEvent(fizz="buzz")

    event_bus(event=event1)
    event_bus(event=event2)

    subscriber1_mock.assert_called_with(event1)
    subscriber2_mock.assert_called_with(event2)
    assert subscriber1_mock.call_count == 1
    assert subscriber2_mock.call_count == 1
