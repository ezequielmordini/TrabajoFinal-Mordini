from django.test import TestCase
from django.urls import reverse

class AboutViewTests(TestCase):
    def test_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_view_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_about_view_contains_expected_content(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertContains(response, "¡Hola! Soy Ezequiel Mordini")
