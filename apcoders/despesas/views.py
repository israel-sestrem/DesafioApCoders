from django.shortcuts import render, redirect
from .models import Despesa
from .forms import FormDespesa
from unidades.models import Unidade

# Create your views here.

def listar_despesas(request):
    despesas = Despesa.objects.all().order_by('id_unidade')
    totalDespesas = Despesa.objects.all().count()
    valorTotal = 0
    for despesa in despesas:
        valorTotal += despesa.valor
    dados = {
        'despesas' : despesas,
        'totalDespesas' : totalDespesas,
        'valorTotal' : valorTotal
    }
    return render(request,'despesas/inicio.html', dados)

def cadastrar_despesas(request):
    if ( request.method == 'POST' ):
        form = FormDespesa(request.POST)
        if ( form.is_valid() ):
            idUnidade = int(form['id_unidade'].value())
            unidades = Unidade.objects.all()
            for unidade in unidades:
                if ( unidade.id == idUnidade ):
                    form.save()
                    return redirect('listarDespesas')
            return redirect('unidadeNaoExiste')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'despesas/cadastrar_despesas.html')

def editar_despesas(request, id):
    despesa = Despesa.objects.get(id=id)
    if ( request.method == 'POST' ):
        form = FormDespesa(request.POST, instance=despesa)
        if ( form.is_valid() ):
            idUnidade = int(form['id_unidade'].value())
            unidades = Unidade.objects.all()
            for unidade in unidades:
                if ( unidade.id == idUnidade ):
                    form.save()
                    return redirect('listarDespesas')
            return redirect('unidadeNaoExiste')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'despesas/editar_despesas.html', {'despesa' : despesa})

def deletar_despesas(request, id):
    despesa = Despesa.objects.get(id=id)
    if ( request.method == 'POST' ):
        despesa.delete()
        return redirect('listarDespesas')
    else:
        return render(request, 'despesas/deletar_despesas.html', {'despesa' : despesa})