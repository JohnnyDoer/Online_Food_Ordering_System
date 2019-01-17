
# Create your tests here.
import unittest
from django.contrib.auth.models import User
from django.test import TestCase, Client
from Customers.models import Area, City, Item, Order, Food, Restaurant, FoodCategory, Profile, Address
from django.contrib.auth.models import User


class DeliveryPageTests(TestCase):
    def setUp(self):
        pass

    def test_delivery_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_delivery_signup(self):
        c = Client()
        response = c.post(
            '/delivery/signup/', {'username': 'save12', 'email': 'eede@gmail.com', 'password': 'asdfghjkl12'})
        self.assertEquals(response.status_code, 200)

    def test_delivery_random_url(self):
        response = self.client.get('/randomname/')
        self.assertEquals(response.status_code, 404)

    def test_delivery_random_urlentrywithnumbers(self):
        response = self.client.get('/wheer4354e/')
        self.assertEquals(response.status_code, 404)


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.createadmin = User.objects.create(
            username="qwerefty", email="test@gmil.com", password="asdfefghjkl")
        self.client = None
        self.request_url = '/delivery/'
        self.client = Client()

    def test_check(self):
        self.client = Client()
        response = self.client.get('delivery/somesite')
        self.assertEqual(response.status_code, 404)
