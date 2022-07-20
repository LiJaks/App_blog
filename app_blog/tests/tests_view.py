from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from app_blog.models import BlogRecordModel, BlogImgModel, UploadRecord
from django.core.files.uploadedfile import SimpleUploadedFile


USER = {
    'username': 'TestingUser4',
    'first_name': 'Michael',
    'last_name': 'Bisping',
    'email': 'testBisp@mail.ru',
    'password': 'zc6-XU2-DTQ-Ae6',
}


class BlogViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(**USER)

    def setUp(self):
        self.client.login(username='TestingUser4', password='zc6-XU2-DTQ-Ae6')

    def test_create_record(self):
        url = reverse('create_url')

        with open('files_for_tests/img/ava2.png', 'rb') as img2_b:
            img2 = SimpleUploadedFile("ava2.png", img2_b.read(), content_type="image/png")

        with open('files_for_tests/img/ava3.png', 'rb') as img3_b:
            img3 = SimpleUploadedFile("ava3.png", img3_b.read(), content_type="image/png")

        record_1 = {'title': 'Test',
                    'description': 'TestTestTestTestTestTestTestTestTestTestTest',
                    'images': [img2, img3]
                    }

        response = self.client.post(url, record_1)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

        self.assertEqual(len(BlogRecordModel.objects.all()), 1)
        self.assertEqual(str(BlogRecordModel.objects.first().user),'TestingUser4')

        self.assertEqual(len(BlogImgModel.objects.all()), 2)

    def test_upload_records(self):
        url = reverse('upload_url')

        with open('files_for_tests/records/tests_records.csv', 'rb') as file_csv_b:
            file_records = SimpleUploadedFile("tests_records.csv", file_csv_b.read(), content_type='text/csv')

        response = self.client.post(url, {'file': file_records})
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(UploadRecord.objects.all()), 1)

        self.assertEqual(len(BlogRecordModel.objects.all()), 5)
