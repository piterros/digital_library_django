from .models import Games, Books, Videos
from .serializer import GamesSerializer, BooksSerializer, VideosSerializer

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from django.core.exceptions import FieldError


class CustomMethods:
    def search(self, serializer, model, search_key, search_value):
        if search_key and search_value:
            try:
                queryset = model.filter(**{search_key: search_value})
            except FieldError:
                return Response(
                    {"search_result": "incorrect key"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            result = serializer(queryset, many=True).data
            if result:
                return Response(result, status=status.HTTP_200_OK)
            return Response(
                {"search_result": "no data"}, status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            {"search_result": "key and/or value not specified"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

    @action(detail=False, methods=["get"], url_path="search")
    def search_games(self, request: Request, *args, **kwargs):
        return CustomMethods().search(
            serializer=GamesSerializer,
            model=Games.objects,
            search_key=request.query_params.get("key"),
            search_value=request.query_params.get("value"),
        )


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

    @action(detail=False, methods=["get"], url_path="search")
    def search_books(self, request: Request, *args, **kwargs):
        return CustomMethods().search(
            serializer=BooksSerializer,
            model=Books.objects,
            search_key=request.query_params.get("key"),
            search_value=request.query_params.get("value"),
        )


class VideosViewSet(ModelViewSet):
    serializer_class = VideosSerializer
    queryset = Videos.objects.all()

    @action(detail=False, methods=["get"], url_path="search")
    def search_videos(self, request: Request, *args, **kwargs):
        return CustomMethods().search(
            serializer=VideosSerializer,
            model=Videos.objects,
            search_key=request.query_params.get("key"),
            search_value=request.query_params.get("value"),
        )
