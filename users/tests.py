from django.urls import reverse
from rest_framework import status

from users.models import CustomUser
from rest_framework.test import APITestCase


class EmailIsUsedViewTestCase(APITestCase):
    list_url = reverse("email-exists")

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="taras", password="qwerty13", email="test@gmail.com")

    def test_user_exists(self):
        message = {"message": "A user with that username already exists"}
        response = self.client.post(self.list_url, {"username": "taras"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.message, message)

    def test_user_does_not_exists(self):
        message = {}
        response = self.client.post(self.list_url, {"username": "taras"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.message, message)


class UsernameIsUsedViewTestCase(APITestCase):
    list_url = reverse("user-exists")

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="taras", password="qwerty13", email="test@gmail.com")

    def test_email_exists(self):
        message = {"message": "A user is already registered with this e-mail address."}
        response = self.client.post(self.list_url, {"email": "katrychtaras@gmail.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], message)

    def test_email_does_not_exists(self):
        message = {}
        response = self.client.post(self.list_url, {"email": "katrychtaras@gmail.com"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], message)
