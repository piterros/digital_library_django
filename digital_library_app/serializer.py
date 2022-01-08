from rest_framework.serializers import ModelSerializer

from .models import Games, Books, Videos

class GamesSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"