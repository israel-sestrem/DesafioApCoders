from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.

class Despesa(models.Model):
    id_unidade = IntegerField()
    descricao = CharField(max_length=100)
    tipo_despesa = CharField(max_length=30)
    valor = IntegerField()
    vencimento_fatura = DateField()
    status_pagamento = CharField(max_length=30)

    class Meta:
        db_table = 'despesas'