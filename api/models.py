from django.db import models
import uuid

# Create your models here.

class Livros(models.Model):
    GENEROS_CHOICES = [
        ('romance', 'Romance'),
        ('aventura', 'Aventura'),
        ('autoajuda', 'Auto Ajuda'),
        ('infantil', 'Infantil'),
        ('ficcao', 'Ficção'),
        ('quadrinho', 'História em quadrinho'),
        ('religiao', 'Religião'),
        ('terror', 'Terror'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )

    nome = models.CharField(
        max_length=50,
        null=True,
        blank=False
    )

    genero = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=GENEROS_CHOICES
    )

    editora = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    
    autor = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    data_publicacao = models.DateField(
        null=False,
        blank=True
    )

    qtd_paginas = models.IntegerField(
        null=False,
        blank=False
    )