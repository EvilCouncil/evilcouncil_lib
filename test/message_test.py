import unittest
from eclib.msg import notification
from eclib.msg import routing_keys


class TestMessage(unittest.TestCase):
    def test_message(self):
        note = notification.Notification(msg="test message")
        actual_msg = note.get_message()
        self.assertEqual(actual_msg, '{"message": "test message"}')
        self.assertEqual(note.get_routing_key(), routing_keys.RoutingKeys.NOTIFICATION)
