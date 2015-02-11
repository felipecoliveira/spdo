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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sigla', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fluxo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Observacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
            name='PessoaDestino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pessoa', models.ForeignKey(to='core.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PessoaOrigem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pessoa', models.ForeignKey(to='core.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
            name='Referencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('protocolo', models.ForeignKey(to='core.Protocolo', related_name='protocolo')),
                ('referencia', models.ForeignKey(to='core.Protocolo', related_name='referencia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('data', models.DateTimeField()),
                ('pessoa', models.ForeignKey(to='core.Pessoa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=40)),
                ('inicial', models.IntegerField()),
                ('final', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEntrega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('data_disponibilidade', models.DateTimeField()),
                ('data_recebimento', models.DateTimeField()),
                ('acao', models.CharField(max_length=2000)),
                ('copia', models.IntegerField()),
                ('usuario', models.CharField(max_length=40)),
                ('area', models.ForeignKey(to='core.Area', related_name='area')),
                ('area_anterior', models.ForeignKey(related_name='area_anterior', to='core.Area', null=True)),
                ('protocolo', models.ForeignKey(to='core.Protocolo')),
                ('responsavel', models.ForeignKey(to='core.Responsavel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TramiteInbox',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('area', models.ForeignKey(to='core.Area')),
                ('protocolo', models.ForeignKey(to='core.Protocolo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TramiteOutbox',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('area', models.ForeignKey(to='core.Area')),
                ('protocolo', models.ForeignKey(to='core.Protocolo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transicao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('area_destino', models.ForeignKey(to='core.Area', related_name='area_destino')),
                ('area_origem', models.ForeignKey(to='core.Area', related_name='area_origem')),
                ('fluxo', models.ForeignKey(to='core.Fluxo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='situacao',
            field=models.ForeignKey(to='core.Situacao'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='protocolo',
            name='tipo_documento',
            field=models.ForeignKey(to='core.TipoDocumento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoaorigem',
            name='protocolo',
            field=models.ForeignKey(to='core.Protocolo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoadestino',
            name='protocolo',
            field=models.ForeignKey(to='core.Protocolo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoadestino',
            name='tipo_entrega',
            field=models.ForeignKey(to='core.TipoEntrega'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='uf',
            field=models.ForeignKey(to='core.Uf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notificacao',
            name='pessoa',
            field=models.ForeignKey(to='core.Pessoa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notificacao',
            name='protocolo',
            field=models.ForeignKey(to='core.Protocolo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fluxo',
            name='tipo_documento',
            field=models.ForeignKey(to='core.TipoDocumento'),
            preserve_default=True,
        ),
    ]
