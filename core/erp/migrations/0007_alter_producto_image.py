# Generated by Django 4.0.3 on 2022-04-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/product/%Y/%m/%d', verbose_name='Image'),
        ),
    ]
