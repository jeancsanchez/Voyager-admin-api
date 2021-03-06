# Generated by Django 2.1.4 on 2018-12-21 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentoViagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objetivo', models.CharField(max_length=100, verbose_name='Objetivo da viagem')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Documento de viagem (DV)',
                'verbose_name_plural': 'Documentos de viagem',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('matricula', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TipoViagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trajeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateTimeField(verbose_name='Data da saida')),
                ('data_chegada', models.DateTimeField(verbose_name='Data da chegada')),
                ('chegada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chegada',
                                              to='voyage.Cidade')),
                ('saida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saida',
                                            to='voyage.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='voyage.Funcionario')),
            ],
            bases=('voyage.funcionario',),
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('funcionario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='voyage.Funcionario')),
            ],
            bases=('voyage.funcionario',),
        ),
        migrations.AddField(
            model_name='documentoviagem',
            name='solicitante',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE,
                                       related_name='solicitante', to='voyage.Funcionario'),
        ),
        migrations.AddField(
            model_name='documentoviagem',
            name='tipo_viagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='voyage.TipoViagem',
                                    verbose_name='Tipo de viagem'),
        ),
        migrations.AddField(
            model_name='documentoviagem',
            name='trajeto',
            field=models.ManyToManyField(to='voyage.Trajeto'),
        ),
        migrations.AddField(
            model_name='documentoviagem',
            name='coordenador',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT,
                                       related_name='coordenador', to='voyage.Coordenador'),
        ),
    ]
