import random

from django.db import models


class Funcionario(models.Model):
    matricula = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=100)


class Agente(Funcionario):
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = '5. Agentes'


class Coordenador(Funcionario):
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = '6. Coordenadores'


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + '-' + self.estado

    class Meta:
        verbose_name_plural = '3. Cidades'


class TipoViagem(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = '2. Tipos de viagens'


class Trajeto(models.Model):
    saida = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='saida')
    data_saida = models.DateTimeField(verbose_name='Data da saida')
    chegada = models.ForeignKey(Cidade, on_delete=models.PROTECT, related_name='chegada')
    data_chegada = models.DateTimeField(verbose_name='Data da chegada')

    def __str__(self):
        return self.saida.nome + ' (' + self.data_saida.strftime('%d/%m/%Y às %H:%M') + ') - ' + \
               self.chegada.nome + '(' + self.data_chegada.strftime('%d/%m/%Y às %H:%M') + ')'

    class Meta:
        verbose_name_plural = '4. Trajetos'


class DocumentoViagem(models.Model):
    tipo_viagem = models.ForeignKey(TipoViagem, on_delete=models.PROTECT, verbose_name='Tipo de viagem')
    solicitante = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='solicitante')
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT, related_name='coordenador')
    trajeto = models.ManyToManyField(to=Trajeto)
    objetivo = models.CharField(max_length=100, verbose_name='Objetivo da viagem')
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.solicitante.nome + '-' + self.tipo_viagem.descricao

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.valor = random.randint(1, 10000)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Documento de viagem (DV)'
        verbose_name_plural = '1. Documentos de viagens'
