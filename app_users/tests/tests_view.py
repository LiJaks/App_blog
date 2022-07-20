from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from app_users.models import ProfileModel


USER = {
    'username': 'TestingUser4',
    'first_name': 'Michael',
    'last_name': 'Bisping',
    'city': 'London',
    'email': 'testBisp@mail.ru',
    'password1': 'Sc6-XU2-DTQ-Ae6',
    'password2': 'Sc6-XU2-DTQ-Ae6',
}

LOG_USER = {
    'username': 'TestingUser3',
    'password': 'zc6-XU2-DTQ-Ae6'
}


class UsersViewTest(TestCase):


    def test_register_view(self):
        url = reverse('register_url')
        response = self.client.post(url, USER)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        self.assertEqual(len(ProfileModel.objects.all()), 1)
        self.assertEqual(str(ProfileModel.objects.first().user),'TestingUser4')

        username = USER['username']
        password = USER['password1']
        self.assertTrue(authenticate(username=username, password=password))

    def setUp(self):
        User.objects.create_user(**LOG_USER)
    def test_login_view(self):
        url = reverse('login_url')
        response = self.client.post(url, LOG_USER, follow=True)
        self.assertTrue(response.context['user'].is_active)
