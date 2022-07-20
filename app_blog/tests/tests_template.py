from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


USER = {
    'username': 'TestingUser4',
    'first_name': 'Michael',
    'last_name': 'Bisping',
    'email': 'testBisp@mail.ru',
    'password': 'zc6-XU2-DTQ-Ae6',
}


class BlogTemplateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(**USER)

    def setUp(self):
        self.client.login(username='TestingUser4', password='zc6-XU2-DTQ-Ae6')

    def test_blog_create_page(self):
        url = reverse('create_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')

    def test_blog_list_page(self):
        url = reverse('list_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'record_list.html')

    def test_blog_upload_page(self):
        url = reverse('upload_url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')
