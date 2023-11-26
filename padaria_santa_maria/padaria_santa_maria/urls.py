from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('lista_usuarios/',views.usuarios,name='listagem_usuarios'),
    path('pedido/',views.pedidos,name='pedidos'),
    path('fila/',views.fila,name='fila'),
    path('cardapio/',views.listas,name='listas'),
    path('feedback/',views.feedback,name='feedback'),
    path('sobrenois/',views.sobrenois,name='sobrenois'),
    path('perfil/',views.perfil,name='perfil')

]
