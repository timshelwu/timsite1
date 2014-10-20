# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyData', '0002_auto_20141020_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stringparameter',
            name='myParent',
            field=models.ForeignKey(verbose_name=b'related StringParameter', to='MyData.DataList'),
        ),
    ]
