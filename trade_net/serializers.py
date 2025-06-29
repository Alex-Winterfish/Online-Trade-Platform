# -*- coding: utf-8 -*-
from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    """Сериализер для model: trade_net.models.Product."""

    class Meta:
        model = models.Product
        fields = ["name", "model", "release_date", "manufacture"]


class NetUnitSerializer(serializers.ModelSerializer):
    """Сериалайзер для model: trade_net.models.NetUnit."""

    produced_prod = ProductSerializer(many=True, read_only=True, source='products')
    retail_prod = serializers.SerializerMethodField()
    def get_retail_prod(self, instance):
        if instance.supplier:
            if instance.supplier.type == 'Завод':
                '''Если внешний ключ модели ссылается напрямую на завод изготовитель.'''
                manuf_id = instance.supplier.id #получаем id завода изготовителя
                queryset = models.Product.objects.filter(manufacture=manuf_id)
                return ProductSerializer(queryset, many=True).data
            elif instance.supplier.type in ['ИП', 'Торговая сеть']:
                '''Если внешний ключ ссылается на поставщика, получаем id завода изготовителя
                от экземпляра модели поставщика.'''
                manuf_id = instance.supplier.supplier.id #получаем id завода изготовителя
                queryset = models.Product.objects.filter(manufacture=manuf_id)
                return ProductSerializer(queryset, many=True).data
        return []

    class Meta:
        model = models.NetUnit
        fields = [
            'id',
            "type",
            "name",
            "email",
            "country",
            "city",
            "address",
            "is_supplier",
            'supplier',
            "dept",
            'produced_prod',
            'retail_prod'
        ]