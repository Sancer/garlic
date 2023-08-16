from unittest import TestCase, mock

from garlic import EventHandler, BaseEvent, EventDispatcher


def subscriber(event: BaseEvent):
    pass


class TestBase(TestCase):

    def setUp(self):
        self.event_handler = EventHandler()
        self.event_dispatcher = EventDispatcher(event_handler=self.event_handler)

    def test_subscription_called(self):
        subscriber_mock = mock.create_autospec(subscriber)
        self.event_handler.subscribe(subscriber=subscriber_mock)

        event = BaseEvent()
        self.event_dispatcher(event=event)

        subscriber_mock.assert_called_once_with(event)

    def test_subscription_called_twice_with_different_events(self):
        subscriber_mock = mock.create_autospec(subscriber)
        self.event_handler.subscribe(subscriber=subscriber_mock)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        subscriber_mock.assert_called_with(event)
        self.assertEqual(subscriber_mock.call_count, 2)

    def test_subscription_called_twice_with_different_events_and_different_subscriptions(self):
        subscriber_mock = mock.create_autospec(subscriber)
        self.event_handler.subscribe(subscriber=subscriber_mock)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        subscriber_mock.assert_called_with(event)
        self.assertEqual(subscriber_mock.call_count, 2)

    def test_two_subscriptions_called(self):
        subscriber_mock = mock.create_autospec(subscriber)
        subscriber_mock2 = mock.create_autospec(subscriber)
        self.event_handler.subscribe(subscriber=subscriber_mock)
        self.event_handler.subscribe(subscriber=subscriber_mock2)

        event = BaseEvent()
        self.event_dispatcher(event=event)

        subscriber_mock.assert_called_once_with(event)
        subscriber_mock2.assert_called_once_with(event)

    def test_two_subscriptions_called_with_different_events(self):
        subscriber_mock = mock.create_autospec(subscriber)
        subscriber_mock2 = mock.create_autospec(subscriber)
        self.event_handler.subscribe(subscriber=subscriber_mock)
        self.event_handler.subscribe(subscriber=subscriber_mock2)

        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        subscriber_mock.assert_called_with(event)
        subscriber_mock2.assert_called_with(event)
        self.assertEqual(subscriber_mock.call_count, 2)
        self.assertEqual(subscriber_mock2.call_count, 2)

    def test_two_subscriptions_called_with_different_events_and_different_subscriptions(self):
        subscriber_mock = mock.create_autospec(subscriber)
        subscriber_mock2 = mock.create_autospec(subscriber)
        self.event_handler.subscribe(subscriber=subscriber_mock)
        self.event_handler.subscribe(subscriber=subscriber_mock2)

        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        subscriber_mock.assert_called_with(event)
        subscriber_mock2.assert_called_with(event)
        self.assertEqual(subscriber_mock.call_count, 2)
        self.assertEqual(subscriber_mock2.call_count, 2)
