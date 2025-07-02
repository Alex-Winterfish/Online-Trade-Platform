# -*- coding: UTF-8 -*-
from rest_framework import status
from rest_framework.test import APITestCase
from trade_net.models import ProductModel, NetUnitModel
from users.models import CustomUser


class NetUnitCRUDTestCase(APITestCase):
    """Тестирование CRUD операций для model:tred_net.models.NetUnitModel."""

    def setUp(self):

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
            pass
