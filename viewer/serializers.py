from django.db.models import CharField, IntegerField, DateField
from rest_framework.fields import IntegerField, CharField, FloatField, DateTimeField
from rest_framework.serializers import Serializer


# do usuni

class ActorSerializer(Serializer):
    id = IntegerField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    phone = CharField()
    salary = FloatField()


class GenerSerializer(Serializer):
    name = CharField()


class MovieSerializer(Serializer):
    title = CharField()
    genre = GenerSerializer()
    rating = IntegerField()
    released = DateField()
    description = CharField()
    created = DateTimeField()

