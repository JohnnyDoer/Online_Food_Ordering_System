
# Create your tests here.
from django.test import TestCase
from .models import Area, City
# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from Restaurants.views import load_areas, index


# The function 'reverse' resolves a view name and its arguments into a path
# which can be passed into the method self.client.get(). We use the 'reverse'
# method here in order to avoid writing hard-coded URLs inside tests.
class RestaurantPageTests(TestCase):
    def setUp(self):
        pass

    def test_restaurant_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_restaurant_signup(self):
        c = Client()
        response = c.post(
            '/restaurant/signup/', {'username': 'save12', 'email': 'eede@gmail.com', 'password': 'asdfghjkl12'})
        self.assertEquals(response.status_code, 200)

    def test_restaurant_random_url(self):
        response = self.client.get('/randomname/')
        self.assertEquals(response.status_code, 404)

    def test_restaurant_random_urlentrywithnumbers(self):
        response = self.client.get('/wheer4354e/')
        self.assertEquals(response.status_code, 404)


class RestaurantAreaViewTests(TestCase):
    def setUp(self):
        super(RestaurantAreaViewTests, self).setUp()
        self.city = City.objects.create(name="Faraday")
        self.city_id = Area.objects.create(name="Grossy", city=self.city)

    def tearDown(self):
        super(RestaurantAreaViewTests, self).tearDown()
        self.city.delete()
        self.city_id.delete()

    def test_post_detail_success(self):
        response = self.client.get(reverse(load_areas), get=self.city)
        # Assert that self.post is actually returned by the post_detail view
        self.assertEqual(response.status_code, 200)


class RestaurantindexViewTests(TestCase):
    def setUp(self):
        super(RestaurantindexViewTests, self).setUp()

    def tearDown(self):
        super(RestaurantindexViewTests, self).tearDown()

    def test_post_detail_success(self):
        response = self.client.get(reverse(index))
        self.assertEqual(response.status_code, 200)
