from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import CustomUser


class UserAPITests(APITestCase):
    def setUp(self):
        # Création d'un utilisateur administrateur
        self.admin_user = CustomUser.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpassword'
        )

        # Création d'un utilisateur normal
        self.normal_user = CustomUser.objects.create_user(
            username='normaluser',
            email='user@example.com',
            password='userpassword'
        )

        # Définir le client
        self.client = APIClient()

    def test_user_registration(self):
        # Test de l'inscription
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123"
        }
        response = self.client.post(reverse('user-register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.filter(username="testuser").exists(), True)

    def test_user_profile_view(self):
        # Authentifier avec un utilisateur normal
        self.client.force_authenticate(user=self.normal_user)

        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.normal_user.username)

    def test_list_all_users_as_admin(self):
        # Authentifier avec l'utilisateur administrateur
        self.client.force_authenticate(user=self.admin_user)

        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)  # On s'attend à voir les deux utilisateurs créés

    def test_list_all_users_as_normal_user(self):
        # Authentifier avec un utilisateur normal
        self.client.force_authenticate(user=self.normal_user)

        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)  # L'utilisateur non-admin ne peut pas accéder à cette vue
