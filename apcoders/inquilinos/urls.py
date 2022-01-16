from django.urls import path
from .views import listar_inquilinos, cadastrar_inquilinos, editar_inquilinos, deletar_inquilinos

urlpatterns = [
    path('cadastrar_inquilinos', cadastrar_inquilinos, name='cadastrarInquilinos'),
    path('editar_inquilinos/<int:id>', editar_inquilinos, name='editarInquilinos'),
    path('deletar_inquilinos/<int:id>', deletar_inquilinos, name='deletarInquilinos'),
    path('', listar_inquilinos, name='listarInquilinos')
]