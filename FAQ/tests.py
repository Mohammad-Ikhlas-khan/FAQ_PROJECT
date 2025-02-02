from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQModelTest(TestCase):
    def test_auto_translation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )
        self.assertTrue(faq.question_hi)
        self.assertTrue(faq.answer_bn)

class FAQAPITest(TestCase):
    def test_api_response(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)