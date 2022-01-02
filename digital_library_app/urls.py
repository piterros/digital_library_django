from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import GamesViewSet


router = DefaultRouter()
router.register(Games, GamesViewSet, base_name='company')

urlpatterns = [
    re_path('^', include(router.urls)),
]