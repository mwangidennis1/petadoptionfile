from django.test import TestCase
from django.urls import reverse
from django.test import SimpleTestCase

class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self): 
        response = self.client.get('/')
        self.assertEqual(response.status_code,  200)


    def test_homepage_url_name(self):
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code,  200)
    def test_homepage_template(self):
        response=self.client.get("/")
        self.assertTemplateUsed(response,'home.html')    


