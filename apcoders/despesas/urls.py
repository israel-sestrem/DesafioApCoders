from django.urls import path
from .views import listar_despesas, cadastrar_despesas, editar_despesas, deletar_despesas

urlpatterns = [
    path('cadastrar_despesas', cadastrar_despesas, name='cadastrarDespesas'),
    path('editar_despesas/<int:id>', editar_despesas, name='editarDespesas'),
    path('deletar_despesas/<int:id>', deletar_despesas, name='deletarDespesas'),
    path('', listar_despesas, name='listarDespesas')
]