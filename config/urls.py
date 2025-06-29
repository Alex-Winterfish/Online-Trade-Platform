from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("trade_net.urls", namespace="trade_net")),
    # path('', include('users.urls', namespace='users'))
]
