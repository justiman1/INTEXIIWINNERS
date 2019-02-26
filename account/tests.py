from django.test import TestCase
from account import models as amod
from datetime import datetime
from lxml import etree

class AccountTests(TestCase):
    fixtures = [ 'account.yaml' ]

    def setUp(self):
        # I'm creating a user here (instead of use one from the fixtures)
        # because you students probably don't have the same users in fixtures.
        self.homer = amod.User()
        self.homer.username = "homer2"
        self.homer.set_password('doh!')
        self.homer.first_name = "Homer"
        self.homer.last_name = "Simpson"
        self.homer.birthdate = datetime(2000, 1, 1)
        self.homer.save()

    def test_user(self):
        u = amod.User()
        u.username = 'bart'
        u.first_name = 'Bart'
        u.last_name = 'Simpson'
        u.set_password('eatmyshorts')
        u.save()
        u.check_password('eatmyshorts')

    def test_user_login(self):
        credentials = {
            'username': 'homer2',
            'password': 'doh!'
        }
        response = self.client.post('/account/login/', credentials)
        # get the request object (testing framework embeds it as response.wsgi_request)
        request = response.wsgi_request
        # this next line is ONLY for debugging the test - it should be removed after things work
        self.print_html(response.content)
        # if it worked, then request.user will be the homer object and is_authenticated will be true
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.homer.id, msg="User should have been homer")
        # if it worked, the response should be a redirect code (login.py returned HttpResponseRedirect)
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

    def print_html(self, content):
        '''Helper to pretty-print HTML'''
        content = content.strip()
        if content:
            html = etree.HTML(content)
            print(etree.tostring(html, pretty_print=True, encoding=str))
        else:
            print('<empty content>')

    # @classmethod
    # def setUpTestData(cls):
    #     # Set up data for the whole TestCase
    #     cls.foo = Foo.objects.create(bar="Test")
    #     ...

    def test_user_get(self):
        u1 = amod.User.objects.get(id=2)
        self.assertEqual(u1.username, 'homer', msg="Username should have been homer")
        self.assertEqual(u1.check_password(''), msg="Wrong password")

    def test_user_create(self):
        u1 = amod.User()
        u1.username = 'luke'
        u1.save()
        u2 = amod.User.objects.get(id=u1.id)

        self.assertEqual(u1.username, u2.username, msg="Username didn't match")
