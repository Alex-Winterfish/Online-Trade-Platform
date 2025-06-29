from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from . import models, serializers
class CreateNetUnitView(CreateAPIView):
    '''Контроллер для создания модели объекта сети model:trade_net.models.NetUnit.'''

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer

class RetrieveNetUnitView(RetrieveAPIView):
    '''Контроллер для получение объекта сети model:trade_net.models.NetUnit.'''

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer

class UpdateNetUnitView(UpdateAPIView):
    '''Контроллер для изменения объекта сети model:trade_net.models.NetUnit.'''

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer

class DestroyNetUnit(DestroyAPIView):
    '''Котнтроллер для удаления объекта сети model:trade_net.models.NetUnit.'''

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer
class ListNetUnitView(ListAPIView):
    '''Контроллер для получения списка объекта сети model:trade_net.models.NetUnit.'''

    queryset = models.NetUnit.objects.all()
    serializer_class = serializers.NetUnitSerializer


class CreateProductView(CreateAPIView):
    '''Контроллер для создания модели продукта model:trade_net.models.Product.'''

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class RetrieveProductView(RetrieveAPIView):
    '''Контроллер для получения продукта model:trade_net.models.Product.'''

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class UpdateProductView(UpdateAPIView):
    '''Контроллер для изменения продукта model:trade_net.models.Product.'''

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class DestroyProductView(DestroyAPIView):
    '''Контроллер для удаоения продукта model:trade_net.models.Product.'''

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ListProductView(ListAPIView):
    '''Контроллер для получения списка продуктов model:trade_net.models.Product.'''

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

