from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FilmSerializer, ActorSerializer, GenreSerializer
from .models import Film, Actor, Genre


# from .filters import *


# Create your views here.

class FilmsViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['actor', 'is_published']


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'last_name']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
