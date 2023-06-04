from rest_framework import serializers
from .models import Show, Director, Actor, Theatre


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'surname', 'country', 'image']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname']


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ['id', 'name', 'address', 'city', 'phone', 'image']


class ShowSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    theatre = TheatreSerializer(read_only=True)

    class Meta:
        model = Show
        fields = ['id', 'name', 'annotation', 'language', 'price', 'season',
                  'image', 'premiere', 'ticket_url', 'favourite', 'director', 'theatre']


