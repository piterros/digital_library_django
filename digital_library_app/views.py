from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
# from rest_framework.viewsets import GenericViewSet

from .models import Games, Books, Videos
from .serializer import GamesSerializer, BooksSerializer, VideosSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status

from rest_framework.decorators import action
from typing import Any

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet


# def set_serializer(library_type: str, queryset=None, data=None):
#     if library_type == "games":
#         print('lib type games', flush=True)
#         return GamesSerializer(data=data)
#     if library_type == "books":
#         print('lib type books', flush=True)
#         return BooksSerializer(queryset=queryset, data=data, many=True)


# class MainViewSet(GenericAPIView):
#
#     def get_serializer_class(self, library_type: str):
#         if library_type == "games":
#             print('lib type games', flush=True)
#             return GamesSerializer(self.get_queryset(), many=True)
#         if library_type == "books":
#             print('lib type books', flush=True)
#             return BooksSerializer(self.get_queryset(), many=True)
#
#     # @action(detail=False, methods=['GET'], url_path="testpath", url_name="testpath")
#     def get(self, request: Request, *args, **kwargs):
#         print('request query params', self.query_params, flush=True)
#         print('request.data', request.data, flush=True)
#         print('kwargs', kwargs, flush=True)
#         serializer = self.get_serializer_class(library_type=self.library_type)
#         return Response(serializer.data)
#
#     def post(self, request: Request, *args, **kwargs):
#         serializer = GamesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request: Request, *args, **kwargs):
#         serializer = GamesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request: Request, *args, **kwargs):
#         serializer = GamesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request: Request, *args, **kwargs):
#         serializer = GamesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.delete()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GetCustomSerializerMixin:
#     actions_and_serializers = {}
#
#     def get_serializer_class(self) -> Any:
#         default = super().get_serializer_class()
#         return self.actions_and_serializers.get(self.action, default)


# class GamesViewSetList(ListAPIView):
#     pass
    # # main_view_set = MainViewSet(library_type="games")
    # serializer_class = GamesSerializer
    # queryset = Games.objects.all()


# class GamesViewSetModify(RetrieveUpdateDestroyAPIView):
#     pass
    # main_view_set = MainViewSet(library_type="games")
    # serializer_class = GamesSerializer
    # queryset = Games.objects.all()
    # def get_queryset(self):
    #     print('get_queryset GamesViewSet 4', flush=True)
    #     return Games.objects.all()
    #
    # def put(self, request: Request, *args, **kwargs):
    #     # serializer = set_serializer(library_type="games", data=request.data)
    #     serializer = GamesSerializer(data=request.data, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request: Request, *args, **kwargs):
    #     serializer = GamesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def get_serializer_class(self):
    #     return GamesSerializer

    # def delete(self, request: Request, pk, *args, **kwargs):
    #     object = self.get_object(pk)
    #
    #     # serializer = GamesSerializer(data=request.data)
    #     # if serializer.is_valid():
    #     #     serializer.delete()
    #         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class VideosViewSet(ModelViewSet):
    serializer_class = VideosSerializer
    queryset = Videos.objects.all()
