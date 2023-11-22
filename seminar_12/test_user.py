"""TestCase класс на основе класса User"""
from unittest import TestCase

from seminar_12.user import User


class UserTestCase(TestCase):
    def test_get_id(self):
        user = User(1, 'John')
        self.assertEqual(user.user_id, 1)

    def test_get_name(self):
        user = User(1, 'John')
        self.assertEqual(user.name, 'John')

    def test_set_id(self):
        user = User(1, 'John')
        user.user_id = 2
        self.assertEqual(user.user_id, 2)

    def test_set_name(self):
        user = User(1, 'John')
        user.name = 'Jane'
        self.assertEqual(user.name, 'Jane')