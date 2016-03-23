# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160315_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='zipcode',
            new_name='zip_code',
        ),
    ]
