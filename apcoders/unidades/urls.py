from django.urls import path
from .views import listar_unidades, cadastrar_unidades, editar_unidades, deletar_unidades

urlpatterns = [
    path('cadastrar_unidades', cadastrar_unidades, name='cadastrarUnidades'),
    path('editar_unidades/<int:id>', editar_unidades, name='editarUnidades'),
    path('deletar_unidades/<int:id>', deletar_unidades, name='deletarUnidades'),
    path('', listar_unidades, name='listarUnidades')
]