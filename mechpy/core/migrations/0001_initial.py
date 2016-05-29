# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('codigo_ibge', models.CharField(blank=True, max_length=30, null=True, verbose_name='Código IBGE')),
            ],
            options={
                'verbose_name_plural': 'Cidades',
                'verbose_name': 'Cidade',
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
            ],
            options={
                'verbose_name_plural': 'Contatos',
                'verbose_name': 'Contato',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('numero', models.CharField(max_length=50, verbose_name='Número')),
                ('rua', models.CharField(max_length=100, verbose_name='Rua')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cep', models.CharField(max_length=20, verbose_name='Cep')),
                ('cidade', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Cidade', verbose_name='Cidade')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
                'verbose_name': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=2, verbose_name='Sigla')),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=2, verbose_name='Sigla')),
            ],
            options={
                'verbose_name_plural': 'Países',
                'verbose_name': 'País',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('tipo', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'verbose_name': 'Pessoa',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pessoa_fisica', serialize=False, to='core.Pessoa', verbose_name='Pessoa Física')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('cpf', models.IntegerField(blank=True, null=True, verbose_name='CPF')),
            ],
            options={
                'verbose_name_plural': 'Pessoas Físicas',
                'verbose_name': 'Pessoa Física',
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pessoa_juridica', serialize=False, to='core.Pessoa', verbose_name='Pessoa Jurídica')),
                ('cnpj', models.IntegerField(blank=True, null=True, verbose_name='CNPJ')),
                ('razao_social', models.CharField(max_length=200, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(max_length=200, verbose_name='Nome Fantasia')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('inscricao_estadual', models.CharField(max_length=30, verbose_name='Inscrição Estadual')),
                ('inscricao_municipal', models.CharField(max_length=30, verbose_name='Inscrição Municipal')),
            ],
            options={
                'verbose_name_plural': 'Pessoas Jurídicas',
                'verbose_name': 'Pessoa Jurídica',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estados', to='core.Pais'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cidades', to='core.Estado'),
        ),
    ]
