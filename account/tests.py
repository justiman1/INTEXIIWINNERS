from django.test import TestCase
from account import models as amod


class AccountTests(TestCase):
    fixtures = ['account.yaml']

    # @classmethod
    # def setUpTestData(cls):
    #     # Set up data for the whole TestCase
    #     cls.foo = Foo.objects.create(bar="Test")
    #     ...

    def test_user_get(self):
        u1 = amod.User.objects.get(id=2)
        self.assertEqual(u1.username, 'homer', msg="Username should have been homer")
        self.assertEqual(u1.check_password(''), message="Wrong password")

    def test_user_create(self):
        u1 = amod.User()
        u1.username = 'luke'
        u1.save()
        u2 = amod.User.objects.get(id=u1.id)

        self.assertEqual(u1.username, u2.username, msg="Username didn't match")
