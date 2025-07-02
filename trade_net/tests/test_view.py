# -*- coding: UTF-8 -*-
from rest_framework import status
from rest_framework.test import APITestCase
from trade_net.models import ProductModel, NetUnitModel
from users.models import CustomUser


class NetUnitCRUDTestCase(APITestCase):
    """Тестирование CRUD операций для model:tred_net.models.NetUnitModel."""

    def setUp(self):

        user = {
                "email": "user_1@mail.com",
                "username": "User_1",
                "password": "pbkdf2_sha256$870000$cXDyxcfpSsVnOEgcjD0hd9$e8pQZzj6Q5G5P9MYSjAhJ7He5FEOxhktOcasUGtOxAQ=",
                "country": "Russia",
                "is_staff": True
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

    def test_get_netunit(self):
        '''Тестирование проверяет получение списка model:trade_net.models.NetUnitModel.'''

        request = self.client.get('/net-unit-list/')
        print(request.__dict__)
        self.assertEqual(request.status_code,status.HTTP_200_OK)
