# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cineREST', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='on_screen',
            field=models.BooleanField(default=True),
        ),
    ]
