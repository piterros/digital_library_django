from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Games, Books, Videos
from .serializer import GamesSerializer

class GamesViewSet(GenericViewSet,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   ListModelMixin):

    serializer_class = GamesSerializer
    queryset = Games.objects.all()
