# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyData', '0005_auto_20141020_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('myParent', models.ForeignKey(to='MyData.DataList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
