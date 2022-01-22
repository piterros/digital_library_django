# from django.conf.urls import include, re_path
# from rest_framework.routers import DefaultRouter
# from .views import GamesViewSet
#
#
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from digital_library_app import views
# #
# #
# # router = DefaultRouter()
# # router.register(Games, GamesViewSet, base_name='company')
# #
# # urlpatterns = [
# #     re_path('^', include(router.urls)),
# # ]
#
# router = DefaultRouter()
# router.register(r'games', GamesViewSet)
# urlpatterns = [
#     path('games/', views.GamesViewSet.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from digital_library_app import views
#
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'games', views.GamesViewSet)
# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]
