from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    telefone = models.TextField(max_length=255)
    endereco = models.TextField(max_length=255)
    pedido = models.TextField()
    pagamento = models.TextField()

