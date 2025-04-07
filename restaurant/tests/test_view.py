from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setupTestData(self):
        # Create test instances of the Menu model
        MenuItem.objects.create(title="Pasta", price=12.99, inventory=10)
        MenuItem.objects.create(title="Pizza", price=9.99, inventory=15)
        MenuItem.objects.create(title="Salad", price=7.99, inventory=20)

    def test_getall(self):
        # Retrieve all Menu objects
        menus = MenuItem.objects.all()
        serialized_menus = MenuItemSerializer(menus, many=True).data

        # Make a GET request to the Menu endpoint
        response = self.client.get('localhost:8000/restaurant/menu/')  # Adjust the endpoint as needed

        # Assert that the serialized data matches the response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_menus)