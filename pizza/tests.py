from django.test import TestCase

# test.py
from django.test import TestCase
from django.urls import reverse
from .models import PizzaPie, MenuItem, Order

class PizzaPieModelTest(TestCase):
    def setUp(self):
        self.pizzapie = PizzaPie.objects.create(name="PizzaPie", address="123 Main St")

    def test_pizzapie_creation(self):
        self.assertEqual(self.pizzapie.name, "PizzaPie")
        self.assertEqual(self.pizzapie.address, "123 Main St")

class MenuItemModelTest(TestCase):
    def setUp(self):
        self.pizzapie = PizzaPie.objects.create(name="PizzaPie", address="123 Main St")
        self.menuitem = MenuItem.objects.create(restaurant=self.pizzapie, name="Pizza Margherita", description="Classic margherita pizza", price=10.99)

    def test_menuitem_creation(self):
        self.assertEqual(self.menuitem.restaurant.name, "PizzaPie")
        self.assertEqual(self.menuitem.name, "Pizza Margherita")
        self.assertEqual(self.menuitem.description, "Classic margherita pizza")
        self.assertEqual(self.menuitem.price, 10.99)

class OrderModelTest(TestCase):
    def setUp(self):
        self.pizzapie = PizzaPie.objects.create(name="PizzaPie", address="123 Main St")
        self.order = Order.objects.create(restaurant=self.pizzapie, customer_name="John Doe", customer_address="456 Elm St")

    def test_order_creation(self):
        self.assertEqual(self.order.restaurant.name, "PizzaPie")
        self.assertEqual(self.order.customer_name, "John Doe")
        self.assertEqual(self.order.customer_address, "456 Elm St")

class OrderViewTest(TestCase):
    def setUp(self):
        self.pizzapie = PizzaPie.objects.create(name="PizzaPie", address="123 Main St")
        self.order = Order.objects.create(restaurant=self.pizzapie, customer_name="John Doe", customer_address="456 Elm St")

    def test_order_list_view(self):
        response = self.client.get(reverse('order-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        



