from django.urls import path
from CadastroCliente import views

urlpatterns = [
    path('', views.index, name = 'index'), #o name aqui é o nome que demos para esse path
    path('Clientes', views.listar_clientes, name='clientes'),
    path('Profissões', views.profissoes, name = 'profissoes'),
    path('cliente/<int:id>', views.detalhar_cliente, name = 'detalhar')
]