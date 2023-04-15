from django.db import models


# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=4)
    estoque = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.nome

