# Generated by Django 4.0.3 on 2022-04-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_categoria_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='desc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
