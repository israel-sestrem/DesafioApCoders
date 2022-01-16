from django.db import models
from django.db.models.fields import CharField, IntegerField, EmailField

# Create your models here.

class Inquilino(models.Model):
    nome = CharField(max_length=50)
    idade = IntegerField()
    sexo = CharField(max_length=20, null=True)
    telefone = IntegerField()
    email = EmailField()

    class Meta:
        db_table = 'inquilinos'
