# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, Client

from Customers.models import Area, City, Item, Order, Food, Restaurant, FoodCategory, Profile, Address


# Url testing
class CustomerPageTests(TestCase):
    def setUp(self):
        pass

    def test_customer_home(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_customer_signup(self):
        c = Client()
        response = c.post(
            '/customer/signup/', {'username': 'save12', 'email': 'eede@gmail.com', 'password': 'asdfghjkl12'})
        self.assertEquals(response.status_code, 200)

    def test_customer_login(self):
        c = Client()
        response = c.post('/customer/login/',
                          {'username': 'save12', 'password': 'asdfghjkl12'})
        self.assertEquals(response.status_code, 200)

    def test_customer_random_url(self):
        response = self.client.get('/randomname/')
        self.assertEquals(response.status_code, 404)

    def test_customer_random_urlentrywithnumbers(self):
        response = self.client.get('/wheer4354e/')
        self.assertEquals(response.status_code, 404)


class AreaTestCase(TestCase):
    @classmethod
    def setUp(self):
        city = City.objects.create(name="Faraday")
        Area.objects.create(city=city, name="Grossy")

    def test_areas_names(self):
        Grossy = Area.objects.get(name="Grossy")
        self.assertEqual(Grossy.city.name, "Faraday")


# Model testing
class ModelsTestCase(TestCase):
    @classmethod
    def setUp(self):
        city = City.objects.create(name="Faraday")
        area = Area.objects.create(city=city, name="Grossy")
        user = User.objects.create(
            username="testuser", email="testuser@gmail.com", password="Hello World")
        Food_Res_ID = Restaurant.objects.create(
            user=user, Restaurant_Name="Bawarchi", Restaurant_Street="fbxfb", Restaurant_Phone_Number="+919440596242")
        Food_Category_ID = FoodCategory.objects.create(
            FoodCategory_Name="Drinks")
        Item_Food_ID = Food.objects.create(
            Food_Name="Milkshake", Food_Price="120", Food_Res_ID=Food_Res_ID, Food_Category_ID=Food_Category_ID)
        Cart_Customer_ID = Profile.objects.create(
            user=user, Customer_First_Name="Thota", Customer_Last_Name="Chow", Customer_Phone_Number="+919440596242")
        Order_Address = Address.objects.create(
            Customer_ID=Cart_Customer_ID, Home="Saddad11", Street="1234", city=city, area=area)
        Item_Order_ID = Order.objects.create(
            Order_Customer_ID=Cart_Customer_ID, Order_Address=Order_Address, Order_Restaurant_ID=Food_Res_ID)
        Item.objects.create(Item_Order_ID=Item_Order_ID,
                            Item_Food_ID=Item_Food_ID, Item_Quantity=3, Item_Price=120)

    def test_items_user(self):
        testuser = Item.objects.get(Item_Price=120)
        self.assertEqual(
            testuser.Item_Order_ID.Order_Customer_ID.user.username, "testuser")

    def test_address_user(self):
        address = Address.objects.get(Home="Saddad11")
        self.assertEqual(address.Street, "1234")

    def test_profile_user(self):
        profile = Profile.objects.get(Customer_First_Name="Thota")
        self.assertEqual(profile.Customer_Last_Name, "Chow")

    def test_City_user(self):
        city = City.objects.get(name="Faraday")
        self.assertEqual(city.name, "Faraday")

    def test_User_user(self):
        user = User.objects.get(email="testuser@gmail.com")
        self.assertEqual(user.password, "Hello World")

    def test_Restaurant_user(self):
        restaurant = Restaurant.objects.get(Restaurant_Name="Bawarchi")
        self.assertEqual(restaurant.Restaurant_Phone_Number, "+919440596242")
