# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyData', '0004_auto_20141020_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stringparameter',
            name='myParent',
            field=models.ForeignKey(to='MyData.DataList'),
        ),
    ]
