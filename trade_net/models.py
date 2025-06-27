from django.db import models

class Manufacture(models.Model):
    '''Модель завода изготовителя'''
    name = models.CharField(verbose_name='Название завода изготовителя', max_length=150)
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(verbose_name='Страна', max_length=100)
    city = models.CharField(verbose_name='Город')
    address = models.CharField(verbose_name='адрес')

    def __str__(self):
        return f'Завод производитель: {self.name}.'

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Product(models.Model):
    '''Модель продукта'''
    name = models.CharField(verbose_name='Название', max_length=200)
    model = models.CharField(verbose_name='Модель', max_length=200)
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    manufacture = models.ForeignKey(verbose_name='Завод изготовитель', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, модель: {self.model}.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetUnit(models.Model):
    '''Модель элемента цепи сбыта'''

    EP = 'ИП' #индивидуальный предприниматель
    RETAIL = 'Торговая сеть' #точка розничной сети

    UNIT_IN_CHOICES = [(EP, 'ИП'), (RETAIL, 'Торговая сеть')]

    type = models.CharField(verbose_name='Собственник', choices=UNIT_IN_CHOICES, max_length=200)
    name = models.CharField(verbose_name='Название', max_length=150)
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(verbose_name='Страна', max_length=100)
    city = models.CharField(verbose_name='Город', max_length=100)
    address = models.CharField(verbose_name='адрес', max_length=300)
    is_supplier = models.BooleanField()
    supplier = models.ForeignKey('trade_net.NetUnit', on_delete=models.SET_NULL, null=True, blank=True)
    dept = models.FloatField(verbose_name='задолженность перед поставщиком', default=0.0)
    created_at = models.DateTimeField(verbose_name='время создания', auto_now_add=True)

    def __str__(self):
        if self.is_supplier:
            return f'Поставщик: {self.type} {self.name}.'
        else:
            return f'Точка сбыта: {self.type} {self.name}.'

    class Meta:
        verbose_name = 'Звено торговой сети'
        verbose_name_plural = 'Торговая сеть'




