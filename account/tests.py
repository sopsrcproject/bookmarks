from django.test import TestCase
from django.contrib.staticfiles import finders


class TestStaticFiles(TestCase):
    """Check if app contains required static files"""
    def test_css(self):
        abs_path = finders.find('css/base.css')
        self.assertIsNotNone(abs_path)
