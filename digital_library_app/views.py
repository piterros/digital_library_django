from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .models import Games, Books, Videos
from .serializer import GamesSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status


class GamesViewSet(GenericAPIView):

    def get_queryset(self):
        return Games.objects.all()

    def get_serializer_class(self):
        return GamesSerializer

    def get(self, request: Request, *args, **kwargs):
        serializer = GamesSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, *args, **kwargs):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args, **kwargs):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, *args, **kwargs):
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)