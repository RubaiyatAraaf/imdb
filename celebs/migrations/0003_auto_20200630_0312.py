# Generated by Django 3.0.7 on 2020-06-30 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0002_auto_20200628_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='imdb_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=15, verbose_name='IMDB Id'),
        ),
    ]
