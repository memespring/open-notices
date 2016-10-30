from django.test import TestCase
from django.test import Client
from notices import models

# Create your tests here.
class NoticeTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_list(self):
        response = self.client.get('/notices/')
        self.assertEqual(response.status_code, 200)

    def test_view_notice(self):
        notice = models.Notice()
        notice.title = 'test title'
        notice.details = 'test details'
        notice.location = 'SRID=3857;POINT (-284821.3533571999869309 6865433.3731604004278779)'
        notice.save()

        response = self.client.get('/notices/%s/' % notice.pk)
        self.assertContains(response, 'test title', 2, 200)
        self.assertEqual(response.status_code, 200)



    def test_create_empty(self):
        response = self.client.post('/notices/new')
        self.assertContains(response, "This field is required", 2, 200)
        self.assertContains(response, "No geometry value provided", 1, 200)

    def test_create_valid(self):
        data =  {'title': 'Test notice', 'details': 'It is a test', 'location': 'SRID=3857;POINT (-284821.3533571999869309 6865433.3731604004278779)'}
        response = self.client.post('/notices/new', data)
        self.assertEqual(response.status_code, 302)