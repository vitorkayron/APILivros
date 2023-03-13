from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.serializers import LivroSerializer
from rest_framework import viewsets, permissions
from api.models import Livros

# Create your views here

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nome', 'autor', 'genero']
    search_fields = ['nome', 'autor', 'genero']
    ordering_fields = ['nome',
                       'genero',
                       'editora',
                       'autor',
                       'data_publicacao',
                       'qtd_paginas']
    
