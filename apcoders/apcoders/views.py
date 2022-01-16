from django.shortcuts import render
from unidades.models import Unidade

def inicio(request):
    return render(request, 'principal/index.html')

def form_erro_validacao(request):
    return render(request, 'form_erros/form_erro_validacao.html')

def unidade_nao_existe(request):
    unidades = Unidade.objects.all().order_by('id')
    totalUnidades = Unidade.objects.all().count()
    dados = {
        'unidades' : unidades,
        'totalUnidades' : totalUnidades
    }
    return render(request, 'form_erros/unidade_nao_existe.html', dados)