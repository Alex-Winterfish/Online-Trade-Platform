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


class IsSupplier:
    '''Валидатор проверяет что внешний ключ model:trade_net.models.NetUnit установлен на модель поставщика'''

    def __init__(self, field_sup):
        self.field_sup = field_sup

    def __call__(self, value):
        field_sup = dict(value).get(self.field_sup, False)
        if field_sup:
            if not field_sup.is_supplier:
                raise ValidationError('Объект сети не является поставщиком!')
