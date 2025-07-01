# -*- coding: utf-8 -*-
from rest_framework import serializers
from . import models, validators


class ProductSerializer(serializers.ModelSerializer):
    """Сериализер для model: trade_net.models.Product."""

    class Meta:
        model = models.Product
        fields = ["name", "model", "release_date", "manufacture"]
        validators = validators.IsManufactureValidator


class NetUnitSerializer(serializers.ModelSerializer):
    """Сериалайзер для model: trade_net.models.NetUnit."""

    produced_prod = ProductSerializer(many=True, read_only=True, source='products')
    retail_prod = serializers.SerializerMethodField()
    def get_retail_prod(self, instance):
        if instance.supplier:
            if instance.supplier.unit_type == 'Завод':
                '''Если внешний ключ модели ссылается напрямую на завод изготовитель.'''
                manuf_id = instance.supplier.id #получаем id завода изготовителя
                queryset = models.Product.objects.filter(manufacture=manuf_id)
                return ProductSerializer(queryset, many=True).data
            elif instance.supplier.unit_type in ['ИП', 'Торговая сеть'] and instance.supplier.supplier:
                '''Если внешний ключ ссылается на поставщика, получаем id завода изготовителя
                от экземпляра модели поставщика.'''
                manuf_id = instance.supplier.supplier.id #получаем id завода изготовителя
                queryset = models.Product.objects.filter(manufacture=manuf_id)
                return ProductSerializer(queryset, many=True).data
        return []

    def update(self, instance, validated_data):
        '''Метод запрещает обновление поля dept(задолжность перед поставщиком) при обновлении модели.'''
        validated_data.pop('dept', None)
        return super().update(instance, validated_data)




    class Meta:
        model = models.NetUnit
        fields = [
            'id',
            "unit_type",
            "name",
            "email",
            "country",
            "city",
            "address",
            "is_supplier",
            'supplier',
            "dept",
            'produced_prod',
            'retail_prod',
            'created_at'
        ]

        validators = [
            validators.IsSupplierValidator(field_sup='supplier'),
            validators.NameValidator(field_name='name', field_city='city', field_type='unit_type', field_address='address'),
            validators.AddressValidator(field_address='address')

        ]
