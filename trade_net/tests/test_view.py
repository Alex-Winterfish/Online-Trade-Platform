# -*- coding: UTF-8 -*-
from rest_framework import status
from rest_framework.test import APITestCase
from trade_net.models import ProductModel, NetUnitModel
from users.models import CustomUser


class ModelsCRUDTestCase(APITestCase):
    """Тестирование CRUD операций для model:tred_net.models.NetUnitModel. и над
    model:trade_net.models.ProductModel."""

    def setUp(self):

        user = {
            "email": "user_1@mail.com",
            "username": "User_1",
            "password": "pbkdf2_sha256$870000$cXDyxcfpSsVnOEgcjD0hd9$e8pQZzj6Q5G5P9MYSjAhJ7He5FEOxhktOcasUGtOxAQ=",
            "country": "Russia",
            "is_staff": True,
        }

        self.test_user = CustomUser.objects.create(**user)

        net_units = [
            {
                "unit_type": "Завод",
                "name": "Завод бытовой техники",
                "email": "example_1@gmail.com",
                "country": "Китай",
                "city": "Пекин",
                "address": "ул. Ленина д.2",
            },
            {
                "unit_type": "ИП",
                "name": "Иванов И.И.",
                "email": "example_2@gmail.com",
                "country": "Россия",
                "city": "Москва",
                "address": "ул. Ленина д.2",
                "is_supplier": False,
            },
            {
                "unit_type": "Торговая сеть",
                "name": "М Видео",
                "email": "example_3@gmail.com",
                "country": "Россия",
                "city": "Пермь",
                "address": "ул. Ленина д.2",
                "is_supplier": False,
            },
        ]

        for net_date in net_units:
            NetUnitModel.objects.create(**net_date)

        self.client.force_authenticate(user=self.test_user)

    def test_get_netunit_list(self):
        """Тестирование проверяет получение списка model:trade_net.models.NetUnitModel."""

        request = self.client.get("/net-unit-list/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json().get("count"), 3)

    def test_unit_create(self):
        """Тестирование создание объекта model:trade_net.models.NetUnitModel."""

        test_unit = {
            "unit_type": "Завод",
            "name": "Тестовый объект",
            "email": "example_5@gmail.com",
            "country": "Китай",
            "city": "Пекин",
            "address": "ул. Ленина, д.2",
        }

        request = self.client.post("/net-unit-create/", data=test_unit)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(request.json().get("name"), "Тестовый объект")

    def test_retrieve_unit(self):
        """Тестирование получение объекта model:trade_unit.models.NetUnitModel."""

        request = self.client.get(
            f"/net-unit-retrieve/{NetUnitModel.objects.get(name='Иванов И.И.').id}/"
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json().get("name"), "Иванов И.И.")

    def test_update_unit(self):
        """Тестирование объновдения объекта model:trade_net.models.NetUnitModel."""

        request = self.client.patch(
            f"/net-unit-update/{NetUnitModel.objects.get(name='Иванов И.И.').id}/",
            data={"email": "test@mail.com"},
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json().get("email"), "test@mail.com")

    def test_delete_unit(self):
        """Тестирование удаления объекта model:trade_net.models.NetUnitModel."""

        requests = self.client.delete(
            f"/net-unit-destroy/{NetUnitModel.objects.get(name='Иванов И.И.').id}/"
        )
        self.assertEqual(requests.status_code, status.HTTP_204_NO_CONTENT)

    def test_crate_product(self):
        """Тестирование создания объекта model:trade_net.models.ProductModel."""

        product = {
            "name": "Стиральная машина",
            "model": "Candy M-2",
            "release_date": "2025-06-10",
            "manufacture": NetUnitModel.objects.get(name="Завод бытовой техники").id,
        }

        request = self.client.post("/product-create/", data=product)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        """Тестирование изменения объекта model:trade_net.models.ProductModel."""

        ProductModel.objects.create(
            name="Тестовый продукт",
            model="модель тест",
            release_date="2025-07-12",
            manufacture=NetUnitModel.objects.get(name="Завод бытовой техники"),
        )

        request = self.client.patch(
            f"/product-update/{ProductModel.objects.get(name='Тестовый продукт').id}/",
            data={"model": "модель тест v2"},
        )
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json().get("model"), "модель тест v2")

    def test_delete_product(self):
        """Тестирование удаления объекта model:trade_net.models.ProductModel."""

        ProductModel.objects.create(
            name="Тестовый продукт 2",
            model="модель тест 2",
            release_date="2025-07-12",
            manufacture=NetUnitModel.objects.get(name="Завод бытовой техники"),
        )

        request = self.client.delete(
            f"/product-destroy/{ProductModel.objects.get(name='Тестовый продукт 2').id}/"
        )
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_list_product(self):
        """Тестирование получения списка model:trade_net.models.Product."""

        products = [
            {
                "name": "Test_1",
                "model": "model test 1",
                "release_date": "2025-06-10",
                "manufacture": NetUnitModel.objects.get(name="Завод бытовой техники"),
            },
            {
                "name": "Test_2",
                "model": "model test 2",
                "release_date": "2025-06-10",
                "manufacture": NetUnitModel.objects.get(name="Завод бытовой техники"),
            },
        ]

        for prod_data in products:
            ProductModel.objects.create(**prod_data)

        request = self.client.get("/product-list/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.json().get("count"), 2)
