from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from rest_framework import status
from rest_framework.permissions import AllowAny


class ShowsListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Show.objects.all()
        filter_backends = (SearchFilter, OrderingFilter)
        search_fields = ('name', 'director__name', 'theatre__name')

        check_theatre = self.request.query_params.get('check_theatre', None)
        check_city = self.request.query_params.get('check_city', None)
        check_premiere = self.request.query_params.get('check_premiere', None)
        check_favourite = self.request.query_params.get('check_favourite', None)
        check_director = self.request.query_params.get('check_director', None)

        if check_theatre:
            queryset = queryset.filter(theatre=check_theatre)

        if check_city:
            queryset = queryset.filter(theatre__city=check_city)

        if check_premiere:
            queryset = queryset.filter(premiere=check_premiere)

        if check_favourite:
            queryset = queryset.filter(favourite=check_favourite)

        if check_director:
            queryset = queryset.filter(director=check_director)

        serializer = ShowSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny], )
def hello_django(request):
    print("Request received!")
    return Response({'message:Request successfully returned! Hello Django'}, status=200)


# Show list
@api_view(['GET', 'POST'])
def show_list(request, format=None):
    if request.method == 'GET':
        shows = Show.objects.all()
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Show details
@api_view(['GET', 'PUT', 'DELETE'])
def show_detail(request, id, format=None):
    try:
        show = Show.objects.get(pk=id)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShowSerializer(show)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShowSerializer(show, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Director list
@api_view(['GET', 'POST'])
def director_list(request, format=None):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Director details
@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id, format=None):
    try:
        director = Director.objects.get(pk=id)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Actor list
@api_view(['GET', 'POST'])
def actor_list(request, format=None):
    if request.method == 'GET':
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Actor details
@api_view(['GET', 'PUT', 'DELETE'])
def actor_detail(request, id, format=None):
    try:
        actor = Actor.objects.get(pk=id)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Theatre list
@api_view(['GET', 'POST'])
def theatre_list(request, format=None):
    if request.method == 'GET':
        theatre = Theatre.objects.all()
        serializer = TheatreSerializer(theatre, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TheatreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Theatre details
@api_view(['GET', 'PUT', 'DELETE'])
def theatre_detail(request, id, format=None):
    try:
        theatre = Theatre.objects.get(pk=id)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TheatreSerializer(theatre)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TheatreSerializer(theatre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        theatre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
