from digital_library_app import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(r"games", views.GamesViewSet)
router.register(r"books", views.BooksViewSet)
router.register(r"videos", views.VideosViewSet)

urlpatterns = router.urls
