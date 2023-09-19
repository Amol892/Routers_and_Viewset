from django.shortcuts import render
from rest_framework import viewsets
from .Serializers import MovieModelSerializer
from .models import Movie
# Create your views here.


class MovieViewsetAPI(viewsets.ModelViewSet):
    serializer_class=MovieModelSerializer
    queryset=Movie.objects.all()
    