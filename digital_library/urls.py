"""digital_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from digital_library_app import views
from rest_framework.routers import DefaultRouter, SimpleRouter

# router = DefaultRouter()
# # router.register(r'games', views.GamesViewSet)
#
# urlpatterns = [
#     path('games/', views.GamesViewSetList.as_view()),
#     path('games/<pk>', views.GamesViewSetModify.as_view()),
#     path('books/', views.BooksViewSet.as_view()),
# ]
# #
# urlpatterns = format_suffix_patterns(urlpatterns)


# router = SimpleRouter()
# router.register(
#     prefix=r"games",
#     viewset=views.GamesViewSet.as_view(),
#     basename="games",
# )
# urlpatterns = router.urls

router = SimpleRouter()
router.register(r'games', views.GamesViewSet)
router.register(r'books', views.BooksViewSet)


urlpatterns = router.urls

