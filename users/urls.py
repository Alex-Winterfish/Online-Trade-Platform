from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig
from users import views
from django.urls import path

app_name = UsersConfig.name

router = SimpleRouter()
router.register("users", views.CustomUserViewSet)

register = views.CustomUserViewSet.as_view({"post": "create"})

urlpatterns = [
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny)),
        name="token_refresh",
    ),
    path("register/", register, name="register"),
] + router.urls
