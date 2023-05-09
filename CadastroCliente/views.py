from django.shortcuts import render

# Create your views here.

def index(request):
    meu_nome = "Caetano"
    lista_frutas = ['Laranja','Maçã','Banana']
    context = {
        'nome': meu_nome,
        'frutas': lista_frutas
    }
    return render(request, 'index.html', context)