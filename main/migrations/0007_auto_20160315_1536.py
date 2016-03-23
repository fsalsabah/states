# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='zipcode',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
