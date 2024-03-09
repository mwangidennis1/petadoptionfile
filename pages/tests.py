from django.test import TestCase
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from .views import HomePageView, AboutPageView 
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

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
 

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Us')


    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual( view.func.__name__,
        AboutPageView.as_view().__name__
        )



