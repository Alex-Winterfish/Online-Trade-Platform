# -*- coding: utf-8 -*-
from rest_framework import serializers
from . import models

class NetUnitSerializer(serializers.ModelSerializer):
    '''Сериалайзер для model: trade_net.models.NetUnit.'''

    class Meta:
        model = models.NetUnit
        fields = [
            'type',
            'name',
            'email',
            'country',
            'city',
            'address',
            'is_supplier',
            'dept',
        ]

class ProductSerializer(serializers.ModelSerializer):
    '''Сериализер для model: trade_net.models.Product.'''

    class Meta:
        model = models.Product
        fields = [
            'name',
            'model',
            'release_date',
            'manufacture'
        ]