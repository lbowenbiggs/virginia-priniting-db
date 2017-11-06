# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VirginiaPrinting', '0003_auto_20171028_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imprintrecord',
            name='id',
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='imprint_number',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=7, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
