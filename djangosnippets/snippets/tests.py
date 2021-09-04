from django.test import TestCase
from django.http import HttpRequest, response
from django.test import TestCase
from snippets.views import top


class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        request = HttpRequest()
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        request = HttpRequest()
        response = self.client.get("/")
        self.assertEqual(response.content, b"hello World")
