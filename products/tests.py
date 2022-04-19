from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command

from products.models import Product, ProductCategory


class TestMainAppSmoke(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'db.json')
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/category/1/')
        self.assertEqual(response.status_code, 200)

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/category/{category.pk}/')
            self.assertEqual(response.status_code, 200)

        # for product in Product.objects.all():
        #     response = self.client.get(f'/products/product/{product.pk}/')
        #     self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'products', 'admins', 'orders', \
                     'baskets')