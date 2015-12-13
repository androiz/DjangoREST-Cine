# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cineREST', '0003_auto_20151208_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='sessions',
            field=models.CharField(default=b'{}', max_length=300),
        ),
    ]
