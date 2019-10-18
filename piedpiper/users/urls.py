

from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserCreateViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)


urlpatterns = [
        path('', include(router.urls)),
        ]
