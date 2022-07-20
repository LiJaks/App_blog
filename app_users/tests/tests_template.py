from django.test import TestCase
from django.urls import reverse


class UsersTemplateTest(TestCase):

    def test_get_main_page(self):
        url = reverse('main_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_get_reg_page(self):
        url = reverse('register_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_get_login_page(self):
        url = reverse('login_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
