from .apps import TradeNetConfig
from django.urls import path
from . import views

app_name = TradeNetConfig.name

urlpatterns = [
    path('net-unit-create/', views.CreateNetUnitView.as_view(), name='net-unit-list'),
    path('net-unit-retrieve/<int:pk>/', views.RetrieveNetUnitView.as_view(), name='net-unit-retrieve'),
    path('net-unit-update/<int:pk>/', views.UpdateNetUnitView.as_view(), name='net-unit-update'),
    path('net-unit-destroy/<int:pk>/', views.DestroyNetUnit.as_view(), name='net-unit-destroy'),
    path('net-unit-list/', views.ListNetUnitView.as_view(), name='net-unit-list'),

    path('product-create/', views.CreateProductView.as_view(), name='product-create'),
    path('product-retrieve/<int:pk>/', views.RetrieveProductView.as_view(), name='product-retrieve'),
    path('product-update/<int:pk>/', views.UpdateProductView.as_view(), name='product-update'),
    path('product-destroy/<int:pk>/', views.DestroyProductView.as_view(), name='product-destroy'),
    path('product-list/<int:pk>/', views.ListProductView.as_view(), name='product-list')
]