from django.shortcuts import render
from rest_framework import viewsets
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):

    queryset = Animal.objects.all().order_by('nome')
    serializer_class = AnimalSerializer

