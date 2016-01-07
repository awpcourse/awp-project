from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class LoginViewTests(TestCase):
    def test_index_redirects_to_login(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/login/?next=/')

    def test_login_successful(self):
        User.objects.create_user(username='Iulia', password='secret')
        response = self.client.post(reverse('login'),
                                    {'username': 'Iulia',
                                     'password': 'secret'})
        self.assertRedirects(response, '/')

    def test_login_failure(self):
        User.objects.create_user(username='Iulia', password='secret')
        response = self.client.post(reverse('login'),
                                    {'username': 'Iulia',
                                     'password': 'fail'})
        self.assertContains(response, 'Wrong username or password')
