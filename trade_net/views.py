# -*- coding: utf-8 -*-
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers
from . import permissions


class CreateNetUnitView(CreateAPIView):
    """Контроллер для создания модели объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)

    def perform_create(self, serializer):
        if self.request.data.get('unit_type') == 'Завод':
            serializer.save(is_supplier=True)


class RetrieveNetUnitView(RetrieveAPIView):
    """Контроллер для получение объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)


class UpdateNetUnitView(UpdateAPIView):
    """Контроллер для изменения объекта сети model:trade_net.models.NetUnit."""
    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)



class DestroyNetUnit(DestroyAPIView):
    """Котнтроллер для удаления объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)

class ListNetUnitView(ListAPIView):
    """Контроллер для получения списка объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['unit_type', 'city', 'country', 'city']
    permission_classes = (permissions.IsActiveStaff,)


class CreateProductView(CreateAPIView):
    """Контроллер для создания модели продукта model:trade_net.models.Product."""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)


class RetrieveProductView(RetrieveAPIView):
    """Контроллер для получения продукта model:trade_net.models.Product."""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)


class UpdateProductView(UpdateAPIView):
    """Контроллер для изменения продукта model:trade_net.models.Product."""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)

class DestroyProductView(DestroyAPIView):
    """Контроллер для удаоения продукта model:trade_net.models.Product."""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)

class ListProductView(ListAPIView):
    """Контроллер для получения списка продуктов model:trade_net.models.Product."""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)