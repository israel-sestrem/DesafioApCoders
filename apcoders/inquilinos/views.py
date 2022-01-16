from django.shortcuts import render, redirect
from .models import Inquilino
from .forms import FormInquilino

# Create your views here.

def listar_inquilinos(request):
    inquilinos = Inquilino.objects.all().order_by('id')
    totalInquilinos = Inquilino.objects.all().count()
    dados = {
        'inquilinos' : inquilinos,
        'totalInquilinos' : totalInquilinos
    }
    return render(request, 'inquilinos/inicio.html', dados)

def cadastrar_inquilinos(request):
    if ( request.method == 'POST' ):
        form = FormInquilino(request.POST)
        if ( form.is_valid() ):
            form.save()
            return redirect('listarInquilinos')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'inquilinos/cadastrar_inquilinos.html')

def editar_inquilinos(request, id):
    inquilino = Inquilino.objects.get(id=id)
    if ( request.method == 'POST' ):
        form = FormInquilino(request.POST, instance=inquilino)
        if ( form.is_valid() ):
            form.save()
            return redirect('listarInquilinos')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'inquilinos/editar_inquilinos.html', {'inquilino' : inquilino})

def deletar_inquilinos(request, id):
    inquilino = Inquilino.objects.get(id=id)
    if ( request.method == 'POST' ):
        inquilino.delete()
        return redirect('listarInquilinos')
    else:
        return render(request, 'inquilinos/deletar_inquilinos.html', {'inquilino' : inquilino})