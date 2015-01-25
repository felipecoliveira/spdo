# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arquivo', models.CharField(max_length=2000)),
                ('tamanho', models.IntegerField()),
                ('data_anexo', models.DateTimeField()),
                ('usuario', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=2000)),
                ('data_observacao', models.DateTimeField()),
                ('usuario', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('endereco', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=30)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('tipo_pessoa', models.CharField(max_length=1)),
                ('contato', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('dv', models.IntegerField()),
                ('numero', models.CharField(max_length=20)),
                ('data_protocolo', models.DateTimeField()),
                ('numero_documento', models.CharField(max_length=20)),
                ('data_emissao', models.DateTimeField()),
                ('assunto', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=50)),
                ('observacao', models.ForeignKey(to='core.Observacao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField()),
                ('pessoa', models.ForeignKey(to='core.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='tipo_documento',
            field=models.ForeignKey(to='core.TipoDocumento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='uf',
            field=models.ForeignKey(to='core.Uf'),
            preserve_default=True,
        ),
    ]
