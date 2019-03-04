from django.test import TestCase
from account import models as amod
from django.contrib.auth import models as pmod
from datetime import datetime
from lxml import etree
from django.contrib.auth.management.commands import changepassword
from django.contrib.auth import models, management
# from StringIO import StringIO

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
        # if it worked, then request.user will be the homer object and is_authenticated will be true
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.homer.id, msg="User should have been homer")
        # if it worked, the response should be a redirect code (login.py returned HttpResponseRedirect)
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected")

    def test_user_logout(self):
        response = self.client.post('/account/logout')
        request = response.wsgi_request
        self.assertTrue(request.user.is_anonymous, msg="User should not be authenticated")

    def test_user_get(self):
        u1 = amod.User.objects.get(id=3)
        self.assertEqual(u1.username, 'user1', msg="Username should have been user0")
        self.assertEqual(u1.password, u1.check_password('asdf'), msg="Wrong password")

    def test_user_create(self):
        u1 = amod.User()
        u1.username = 'luke'
        u1.save()
        u2 = amod.User.objects.get(id=u1.id)

        self.assertEqual(u1.username, u2.username, msg="Username didn't match")


    def test_change_user_password(self):
        u1 = amod.User.objects.get(id=3)

    def test_group_permission(self):
        p = pmod.Permission()
        p.codename = 'NewPermission'
        p.name = 'New Permission'
        p.content_type = pmod.Permission.objects.get(codename = 'add_user').content_type
        p.save()
        g1 = pmod.Group()
        g1.name = 'NewGroup'
        g1.save()
        g1 = pmod.Group.objects.get(name='NewGroup')
        g1.permissions.add(pmod.Permission.objects.get(codename='NewPermission'))
        u1 = amod.User.objects.get(id=3)
        g1 = pmod.Group.objects.get(name='NewGroup')
        u1.groups.add(g1)
        self.assertTrue(u1.has_perm('account.NewPermission'))
