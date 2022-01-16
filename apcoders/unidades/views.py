from django.shortcuts import render, redirect
from .models import Unidade
from .forms import FormUnidade

# Create your views here.

def listar_unidades(request):
    unidades = Unidade.objects.all().order_by('id')
    totalUnidades = Unidade.objects.all().count()
    dados = {
        'unidades' : unidades,
        'totalUnidades' : totalUnidades
    }
    return render(request, 'unidades/inicio.html', dados)

def cadastrar_unidades(request):
    if ( request.method == 'POST' ):
        form = FormUnidade(request.POST)
        if ( form.is_valid() ):
            form.save()
            return redirect('listarUnidades')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'unidades/cadastrar_unidades.html')

def editar_unidades(request, id):
    unidade = Unidade.objects.get(id=id)
    if ( request.method == 'POST' ):
        form = FormUnidade(request.POST, instance=unidade)
        if ( form.is_valid() ):
            form.save()
            return redirect('listarUnidades')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'unidades/editar_unidades.html', {'unidade' : unidade})

def deletar_unidades(request, id):
    unidade = Unidade.objects.get(id=id)
    if ( request.method == 'POST' ):
        unidade.delete()
        return redirect('listarUnidades')
    else:
        return render(request, 'unidades/deletar_unidades.html', {'unidade' : unidade})