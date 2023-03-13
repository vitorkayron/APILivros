from rest_framework import serializers
from api.models import Livros

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = [
            'id',
            'nome',
            'genero',
            'editora',
            'autor',
            'data_publicacao',
            'qtd_paginas',
        ]