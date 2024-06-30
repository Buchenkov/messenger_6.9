from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.test import APIClient
from rest_framework import status


class UserProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_profile(self):
        data = {
            "username": "john_doe",
            "email": "john@example.com",
            "password": "password123",
            "profile": {
                "bio": "Hello, I am John!",
                "avatar": "path/to/avatar.jpg"
            }
        }
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get().bio, 'Hello, I am John!')

    def test_update_user_with_profile(self):
        user = User.objects.create_user(username='john_doe', email='john@example.com', password='password123')
        Profile.objects.create(user=user, bio='Hello, I am John!', avatar='path/to/avatar.jpg')

        data = {
            "username": "john_doe_updated",
            "email": "john_updated@example.com",
            "password": "new_password123",
            "profile": {
                "bio": "Hello, I am John! Updated bio.",
                "avatar": "path/to/new_avatar.jpg"
            }
        }
        response = self.client.put(f'/users/{user.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.username, 'john_doe_updated')
        self.assertEqual(user.profile.bio, 'Hello, I am John! Updated bio.')
