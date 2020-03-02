from django.urls import reverse
from rest_framework.test import APITestCase

from products.models import Product, ProductCategory, ProductSubcategory
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from products.api.serializers import ProductSerializer


class ProductRetrieveUpdateDeleteTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="taras", password="bob")
        self.user1 = CustomUser.objects.create_user(username="bob", password="bob")

        self.token = Token.objects.create(user=self.user)
        self.token1 = Token.objects.create(user=self.user1)

        self.product_category = ProductCategory.objects.create(name="electronic")
        self.product_subcategory = ProductSubcategory.objects.create(product_category=self.product_category,
                                                                     name="cell phone")
        self.product = Product.objects.create(
            seller=self.user,
            name="Iphone500",
            price=20,
            description="some fancy description",
            product_subcategory=self.product_subcategory,
        )
        self.product1 = Product.objects.create(
            seller=self.user,
            name="Iphone600",
            price=200,
            description="some fancy description",
            product_subcategory=self.product_subcategory,
        )
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_authenticated_detail_retrieve(self):
        self.client.force_authenticate(user=self.user)
        serializer_data = ProductSerializer(instance=self.product).data
        response = self.client.get(reverse('product-detail', kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_not_authenticated_detail_retrieve(self):
        self.client.force_authenticate(user=None)
        serializer_data = ProductSerializer(instance=self.product).data
        response = self.client.get(reverse('product-detail', kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_authenticated_but_not_seller_detail_delete(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(reverse('product-detail', kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_seller_detail_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('product-detail', kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_not_authenticated_detail_delete(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse('product-detail', kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_but_not_seller_detail_update(self):
        self.client.force_authenticate(user=self.user1)
        product_update = {
            "name": "Iphone4000",
            "description": "some fancy description",
            "price": 6000,
            "product_subcategory": self.product_category
        }
        response = self.client.put(reverse('product-detail', kwargs={"pk": self.product.id}), data=product_update)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_seller_detail_update(self):
        self.client.force_authenticate(user=self.user)
        product_update = {
            "name": "Iphone4000",
            "description": "some fancy description",
            "price": 6000,
            "product_subcategory": self.product_subcategory.id
        }
        response = self.client.put(reverse('product-detail', kwargs={"pk": self.product.id}), product_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response.data)

    def test_not_authenticated_detail_update(self):
        self.client.force_authenticate(user=None)
        product_update = {
            "name": "Iphone4000",
            "description": "some fancy description",
            "price": 6000,
            "product_subcategory": self.product_category
        }
        response = self.client.put(reverse('product-detail', kwargs={"pk": self.product.id}), data=product_update)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProductListCreateViewTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="taras", password="bob")
        self.token = Token.objects.create(user=self.user)
        self.product_category = ProductCategory.objects.create(name="electronic")
        self.product_subcategory = ProductSubcategory.objects.create(product_category=self.product_category,
                                                                     name="cell phone")
        self.product = Product.objects.create(
            seller=self.user,
            name="Iphone500",
            price=20,
            description="some fancy description",
            product_subcategory=self.product_subcategory,
        )
        self.product1 = Product.objects.create(
            seller=self.user,
            name="Iphone600",
            price=200,
            description="some fancy description",
            product_subcategory=self.product_subcategory,
        )
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_not_authenticated_product_list_retrieve(self):
        response = self.client.get(reverse("product-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_authenticated_product_list_add(self):
        self.client.force_authenticate(user=None)
        new_product = {
            "seller": self.user,
            "name": "Iphone3",
            "description": "some fancy description",
            "price": 500.0,
            "product_subcategory": self.product_subcategory.id
        }
        response = self.client.post(reverse("product-list"), data=new_product)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_product_list_add(self):
        self.client.force_authenticate(user=self.user)
        new_product = {
            "seller": self.user,
            "name": "Iphone3",
            "description": "some fancy description",
            "price": 500.0,
            "product_subcategory": self.product_subcategory.id
        }
        response = self.client.post(reverse("product-list"), data=new_product)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
