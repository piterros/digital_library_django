from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Games, Books, Videos
from .serializer import GamesSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# class GamesViewSet(GenericViewSet,
#                    CreateModelMixin,
#                    RetrieveModelMixin,
#                    UpdateModelMixin,
#                    ListModelMixin):
#
#     serializer_class = GamesSerializer
#     queryset = Games.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class GamesViewSet(GenericAPIView):

    # serializer_class = GamesSerializer
    # queryset = Games.objects.all()

    def get_queryset(self):
        return Games.objects.all()

    def get_serializer(self):
        return GamesSerializer

    def get(self, request, *args, **kwargs):
        serializer = GamesSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response()