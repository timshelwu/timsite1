# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyData', '0003_auto_20141020_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stringparameter',
            name='myParent',
            field=models.ForeignKey(verbose_name=b'relatedStringParameter', to='MyData.DataList'),
        ),
    ]
