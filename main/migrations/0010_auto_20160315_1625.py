# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160315_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='zip_code',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
