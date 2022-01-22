from .models import Games, Books, Videos
from .serializer import GamesSerializer, BooksSerializer, VideosSerializer

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


class CustomMethods:
    def search(self, serializer, model, request):
        if not serializer:
            return Response({"result": "no data"}, status=status.HTTP_204_NO_CONTENT)
        queryset = model.filter(
            **{request.query_params.get("key"): request.query_params.get("value")}
        )
        result = serializer(queryset, many=True).data
        return Response(result, status=status.HTTP_200_OK)


class GamesViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

    @action(detail=False, methods=["get"], url_path="search")
    def search_games(self, request: Request, *args, **kwargs):
        return CustomMethods().search(
            serializer=GamesSerializer, model=Games.objects, request=request
        )


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

    @action(detail=False, methods=["get"], url_path="search")
    def search_books(self, request: Request, *args, **kwargs):
        return CustomMethods().search(
            serializer=BooksSerializer, model=Books.objects, request=request
        )


class VideosViewSet(ModelViewSet):
    serializer_class = VideosSerializer
    queryset = Videos.objects.all()

    @action(detail=False, methods=["get"], url_path="search")
    def search_videos(self, request: Request, *args, **kwargs):
        return CustomMethods().search(
            serializer=VideosSerializer, model=Videos.objects, request=request
        )
