# -*- coding: UTF-8 -*-
from rest_framework import status
from rest_framework.test import APITestCase
from trade_net.models import NetUnitModel
from users.models import CustomUser
from rest_framework.serializers import ValidationError


class ValidatorsTestCase(APITestCase):
    """Тестирование валидаторов."""

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

    def test_is_manufacture(self):
        """Тестирование валидатора trade_net.validators.Is_Manufacture."""

        product = {
            "name": "Test product",
            "model": "Test M-2",
            "release_date": "2025-06-10",
            "manufacture": NetUnitModel.objects.get(name="Иванов И.И.").id,
        }

        request = self.client.post("/product-create/", data=product)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

    def test_is_supplier(self):
        """Тестирование валидатора trade_net.validators.Is_Supplier."""

        test_net_unit = {
            "unit_type": "ИП",
            "name": "Махов И.И.",
            "email": "example_2@gmail.com",
            "country": "Россия",
            "city": "Пермь",
            "address": "ул. Ленина д.2",
            "is_supplier": False,
            "supplier": NetUnitModel.objects.get(name="Иванов И.И.").id,
        }

        request = self.client.post("/net-unit-create/", data=test_net_unit)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

    def test_name_validator_manuf(self):
        """Тестирование валидатора trade_net.validators.NameValidator
        для объекта "Завод"."""

        test_manufacture = {
            "unit_type": "Завод",
            "name": "Завод бытовой техники",
            "email": "example_1@gmail.com",
            "country": "Китай",
            "city": "Пекин",
            "address": "ул. Ленина д.2",
        }

        request = self.client.post("/net-unit-create/", data=test_manufacture)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

    def test_name_validator_trade_net(self):
        """Тестирование валидатора trade_net.validators.NameValidator
        для объекта "Торговая сеть"."""

        test_manufacture = {
            "unit_type": "Торговая сеть",
            "name": "М Видео",
            "email": "example_3@gmail.com",
            "country": "Россия",
            "city": "Пермь",
            "address": "ул. Ленина д.2",
            "is_supplier": False,
        }

        request = self.client.post("/net-unit-create/", data=test_manufacture)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

    def test_address_validator(self):
        """Тестирование валидатора trade_net.validators.AddressValidator"""

        test_unit = {
            "unit_type": "Торговая сеть",
            "name": "М Видео",
            "email": "example_3@gmail.com",
            "country": "Россия",
            "city": "Пермь",
            "address": "Test adress",
            "is_supplier": False,
        }

        request = self.client.post("/net-unit-create/", data=test_unit)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)
