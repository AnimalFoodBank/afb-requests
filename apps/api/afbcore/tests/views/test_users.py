import os
import uuid

from afbcore.serializers import UserSerializer
from afbcore.views.users import CurrentUserAPIView
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

"""
How to run the tests:
    - python manage.py test apps/api/afbcore/tests/views/test_users.py
    - python manage.py test afbcore.tests.views.test_users.RegisterTestCase.test_register_valid_data


"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afbcore.settings")


class RegisterTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        unique_username = "testuser" + str(uuid.uuid4())
        cls.valid_password = "xyz9.helloPLEASE"
        cls.user = User.objects.create(
            username=unique_username,
            email=unique_username + "@example.com",
            password=cls.valid_password,
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        User = get_user_model()
        User.objects.all().delete()
