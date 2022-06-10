"""
Test for models
"""
import email
from operator import imod
from django.test import TestCase #noqa
from django.contrib.auth import get_user_model #noqa


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@apple.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
