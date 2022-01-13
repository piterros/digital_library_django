from rest_framework.serializers import ModelSerializer

from .models import Games, Books, Videos

class GamesSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

class VideosSerializer(ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"