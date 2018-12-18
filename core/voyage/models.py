from django.contrib.auth.models import User
from django.db import models


class Funcionario(User):
    matricula = models.BigIntegerField(primary_key=True)


class Agente(Funcionario):
    pass


class Coordenador(Funcionario):
    pass


class Status(models.Model):
    descricao = models.CharField(max_length=100)


class Origem(models.Model):
    local = models.CharField(max_length=100)
    data = models.DateTimeField(verbose_name='Data e hora')


class Destino(models.Model):
    local = models.CharField(max_length=100)
    data = models.DateTimeField(verbose_name='Data e hora')


class Rota(models.Model):
    origem = models.OneToOneField(Origem, on_delete=models.CASCADE)
    destino = models.OneToOneField(Destino, on_delete=models.CASCADE)


class Roteiro(models.Model):
    objetivo = models.CharField(max_length=100)
    rota = models.ForeignKey(Rota, on_delete=models.PROTECT)


class DocumentoViagem(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    roteiro = models.ForeignKey(Roteiro, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=5)
    solicitante = models.OneToOneField(Funcionario, on_delete=models.CASCADE, related_name='solicitante',
                                       parent_link=True)
    coordenador = models.OneToOneField(Coordenador, on_delete=models.PROTECT, related_name='coordenador',
                                       parent_link=True)

    def __str__(self):
        return self.solicitante.username + '-' + self.status.descricao

    class Meta:
        verbose_name = 'Documento de viagem (DV)'
        verbose_name_plural = 'Documentos de viagem'
