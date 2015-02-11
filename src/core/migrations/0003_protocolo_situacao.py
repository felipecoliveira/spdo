# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_protocolo_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolo',
            name='situacao',
            field=models.ForeignKey(to='core.Situacao', default=1),
            preserve_default=False,
        ),
    ]
