# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 21:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VirginiaPrinting', '0005_auto_20171106_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biography',
            options={'verbose_name_plural': 'biographies'},
        ),
        migrations.AlterModelOptions(
            name='newspaperhistory',
            options={'verbose_name_plural': 'newspaper histories'},
        ),
        migrations.RemoveField(
            model_name='newspapercitation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='newspapercitation',
            name='num_variants',
        ),
        migrations.RemoveField(
            model_name='newspaperhistory',
            name='id',
        ),
        migrations.RemoveField(
            model_name='newspaperhistory',
            name='newspaper_citation',
        ),
        migrations.AddField(
            model_name='biography',
            name='associates',
            field=models.ManyToManyField(related_name='_biography_associates_+', to='VirginiaPrinting.Biography'),
        ),
        migrations.AddField(
            model_name='biography',
            name='first_date',
            field=models.IntegerField(blank=True, default=1700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biography',
            name='formal_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='biography',
            name='function',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='biography',
            name='last_date',
            field=models.IntegerField(blank=True, default=1830),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='biography',
            name='locales',
            field=models.CharField(default='Virginia', max_length=200),
        ),
        migrations.AddField(
            model_name='biography',
            name='precis',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='associates',
            field=models.ManyToManyField(to='VirginiaPrinting.Biography'),
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='description',
            field=models.CharField(default='Unrecorded', max_length=200),
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='issuing_press',
            field=models.CharField(default='Uncertain', max_length=200),
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='place_issued',
            field=models.CharField(default='Virginia', max_length=200),
        ),
        migrations.AddField(
            model_name='imprintrecord',
            name='title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='associates',
            field=models.ManyToManyField(to='VirginiaPrinting.Biography'),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='end_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='frequency',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='lineage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VirginiaPrinting.NewspaperHistory'),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='proprietors',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='start_date',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newspapercitation',
            name='variant_number',
            field=models.CharField(default=1, max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newspaperhistory',
            name='group_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newspaperhistory',
            name='lineage_number',
            field=models.CharField(default=1, max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='biography',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='biography',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='imprintrecord',
            name='pdf_location',
            field=models.FilePathField(path='static/imprints'),
        ),
        migrations.AlterField(
            model_name='imprintrecord',
            name='short_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='newspapercitation',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
