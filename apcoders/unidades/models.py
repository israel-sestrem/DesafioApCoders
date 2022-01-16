from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Unidade(models.Model):
    proprietario = CharField(max_length=50)
    condominio = CharField(max_length=30)
    endereco = CharField(max_length=100)

    class Meta:
        db_table = 'unidades'