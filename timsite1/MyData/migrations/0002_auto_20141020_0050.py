# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decimalparameter',
            name='value',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AlterField(
            model_name='integerparameter',
            name='value',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='stringparameter',
            name='value',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
