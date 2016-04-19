from django.test import TestCase
from django.core.urlresolovers import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.asserEqual(found.func, home_page)

