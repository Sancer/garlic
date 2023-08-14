from unittest import TestCase
from unittest.mock import Mock

from garlic import EventHandler, BaseEvent, EventDispatcher, Subscriber


class TestBase(TestCase):

    def setUp(self):
        self.event_handler = EventHandler()
        self.event_dispatcher = EventDispatcher(event_handler=self.event_handler)

    def test_subscription_called(self):
        mock = Mock(wraps=Subscriber())
        self.event_handler.subscribe(BaseEvent, mock)
        event = BaseEvent()
        self.event_dispatcher(event=event)


        mock.assert_called_once_with(event)

    def test_subscription_called_twice_prevent_duplication(self):
        mock = Mock(wraps=Subscriber())
        self.event_handler.subscribe(BaseEvent, mock)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        self.assertRaises(ValueError, self.event_dispatcher, event=event)

        mock.assert_called_with(event)
        self.assertEqual(mock.call_count, 2)

    def test_subscription_called_twice_with_different_events(self):
        mock = Mock()
        self.event_handler.subscribe(BaseEvent, mock)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        mock.assert_called_with(event)
        self.assertEqual(mock.call_count, 2)

    def test_subscription_called_twice_with_different_events_and_different_subscriptions(self):
        mock = Mock()
        self.event_handler.subscribe(BaseEvent, mock)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        mock.assert_called_with(event)
        self.assertEqual(mock.call_count, 2)

    def test_two_subscriptions_called(self):
        mock = Mock()
        mock2 = Mock()
        self.event_handler.subscribe(BaseEvent, mock)
        self.event_handler.subscribe(BaseEvent, mock2)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        mock.assert_called_once_with(event)
        mock2.assert_called_once_with(event)

    def test_two_subscriptions_called_with_different_events(self):
        mock = Mock()
        mock2 = Mock()
        self.event_handler.subscribe(BaseEvent, mock)
        self.event_handler.subscribe(BaseEvent, mock2)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        mock.assert_called_with(event)
        mock2.assert_called_with(event)
        self.assertEqual(mock.call_count, 2)
        self.assertEqual(mock2.call_count, 2)

    def test_two_subscriptions_called_with_different_events_and_different_subscriptions(self):
        mock = Mock()
        mock2 = Mock()
        self.event_handler.subscribe(BaseEvent, mock)
        self.event_handler.subscribe(BaseEvent, mock2)
        event = BaseEvent()
        self.event_dispatcher(event=event)
        event = BaseEvent()
        self.event_dispatcher(event=event)

        mock.assert_called_with(event)
        mock2.assert_called_with(event)
        self.assertEqual(mock.call_count, 2)
        self.assertEqual(mock2.call_count, 2)