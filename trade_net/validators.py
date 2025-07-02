# -*- coding: utf-8 -*-
import re
from rest_framework.serializers import ValidationError
from . import models

class IsManufactureValidator:
    '''Валидатор установки внешненго ключа модели model:trade_net.models.Product
    на model:trade_net.models.NetUnit, где поле type="Завод".'''
    def __init__(self, field_manuf):
        self.field_manuf = field_manuf

    def __call__(self, value):
        field_manuf = dict(value).get(self.field_manuf, False)

        if field_manuf:
            manuf = models.NetUnit.objects.filter(id=field_manuf.id)
            if manuf.unit_type != 'Завод':
                raise ValidationError('Объект сети не является заводом производителе!')


class IsSupplierValidator:
    '''Валидатор проверяет что внешний ключ model:trade_net.models.NetUnit установлен на модель поставщика'''

    def __init__(self, field_sup):
        self.field_sup = field_sup

    def __call__(self, value):
        field_sup = dict(value).get(self.field_sup, False)
        if field_sup:
            if not field_sup.is_supplier:
                raise ValidationError('Объект сети не является поставщиком!')


class NameValidator:
    '''Валидатор проверяет для объекта сети "Завод" совпадение имен существующих заводов в базе данных.
    Для объекта "Торговая сеть" проверяет совпадение адресов.'''

    def __init__(self, field_type, field_name, field_city, field_address):
        self.field_type = field_type
        self.field_name = field_name
        self.field_city = field_city
        self.field_address = field_address

    def __call__(self, value):
        field_type = dict(value).get(self.field_type, False)
        field_name = dict(value).get(self.field_name, False)
        field_city = dict(value).get(self.field_city, False)
        field_address = dict(value).get(self.field_address, False)

        if field_type == 'Завод':
            if models.NetUnit.objects.filter(name=field_name).exists():
                raise ValidationError('Такой завод производитель уже существует!')
        if field_type == 'Торговая сеть':
            if models.NetUnit.objects.filter(city=field_city, address=field_address).exists():
                raise ValidationError('Магазин торговой сети по этому адресу уже существует!')


class AddressValidator:
    '''Валидатор для заполнеия поля address'''

    def __init__(self, field_address):
        self.field_address = field_address


    def __call__(self, value):
        field_address = dict(value).get(self.field_address, False)
        re_address = re.compile(r'^(ул\.|мкр\.)\s+[А-Яа-яЁё\s]+,\s*(д\.|корп\.|стр\.)\s*\d+$')
        if field_address:
            if not re_address.match(field_address):
                raise ValidationError('Адрес должен иметь вид: ул./мкр."Название", д./корп./стр. "Номер"')
