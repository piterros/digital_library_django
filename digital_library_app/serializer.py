from rest_framework.serializers import ModelSerializer, ValidationError

from .models import Games, Books, Videos


class GamesSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = ["title", "finish_date", "platform", "purchase_date"]

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result["platform"] = result["platform"].upper()
        return result


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ["title", "finish_date", "author", "type", "purchase_date"]

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result["author"] = result["author"].title()
        return result

    def validate(self, instance):
        result = super().to_representation(instance)
        if result["type"] in ("book", "ebook", "audiobook"):
            return result
        raise ValidationError(detail={"Possible book types: book, ebook, audiobook"})


class VideosSerializer(ModelSerializer):
    class Meta:
        model = Videos
        fields = ["title", "finish_date", "type"]

    def validate(self, instance):
        result = super().to_representation(instance)
        if result["type"] in ("movie", "series", "other"):
            return result
        raise ValidationError(detail={"Possible video types: movie, series, other"})
