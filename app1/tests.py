from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_books_page_status_code(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_booksmenu_page_status_code(self):
        response = self.client.get('/booksmenu')
        self.assertEqual(response.status_code, 200)
