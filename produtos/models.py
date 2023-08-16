from django.db import models

# Create your models here.
class Produtos(models.Model):
    numero_produto = models.PositiveBigIntegerField()
    nome_produto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    category = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()

def __str__(self):
    return f'Produto:{ self.nome_produto } { self.marca }'
