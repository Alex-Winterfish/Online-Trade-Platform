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

    queryset = models.NetUnitModel.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)

    def perform_create(self, serializer):
        if self.request.data.get("unit_type") == "Завод":
            serializer.save(is_supplier=True, level='Уровень 0')
        elif self.request.data.get('is_supplier'):
            serializer.save(level='Уровень 1')
        else:
            serializer.save(level='Уровень 2')


class RetrieveNetUnitView(RetrieveAPIView):
    """Контроллер для получение объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnitModel.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)


class UpdateNetUnitView(UpdateAPIView):
    """Контроллер для изменения объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnitModel.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)


class DestroyNetUnit(DestroyAPIView):
    """Котнтроллер для удаления объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnitModel.objects.all()
    serializer_class = serializers.NetUnitSerializer
    permission_classes = (permissions.IsActiveStaff,)


class ListNetUnitView(ListAPIView):
    """Контроллер для получения списка объекта сети model:trade_net.models.NetUnit."""

    queryset = models.NetUnitModel.objects.all()
    serializer_class = serializers.NetUnitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["unit_type", "city", "country", "level"]
    permission_classes = (permissions.IsActiveStaff,)


class CreateProductView(CreateAPIView):
    """Контроллер для создания модели продукта model:trade_net.models.Product."""

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)


class RetrieveProductView(RetrieveAPIView):
    """Контроллер для получения продукта model:trade_net.models.Product."""

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)


class UpdateProductView(UpdateAPIView):
    """Контроллер для изменения продукта model:trade_net.models.Product."""

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)


class DestroyProductView(DestroyAPIView):
    """Контроллер для удаоения продукта model:trade_net.models.Product."""

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)


class ListProductView(ListAPIView):
    """Контроллер для получения списка продуктов model:trade_net.models.Product."""

    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.IsActiveStaff,)
