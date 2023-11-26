from django.shortcuts import render
from .models import Usuario

def pedidos(request):
    return render(request,'pagina/inicial.html')

def home(request):
    return render(request,'pagina/inicial1.html')

def fila(request):
    return render(request,'pagina/fila.html')

def listas(request):
    return render(request,'pagina/listas.html')

def feedback(request):
    return render(request,'pagina/feedback.html')

def sobrenois(request):
    return render(request,'pagina/sobrenois.html')

def perfil(request):
    return render(request,'pagina/perfil.html')


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.telefone = request.POST.get('telefone')
    novo_usuario.endereco = request.POST.get('endereco')
    novo_usuario.pedido = request.POST.get('pedido')
    novo_usuario.pagamento = request.POST.get('pagamento')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'pagina/usuarios.html',usuarios)