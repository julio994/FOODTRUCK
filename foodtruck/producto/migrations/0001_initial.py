# Generated by Django 5.0.4 on 2024-04-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nombre')),
                ('price', models.IntegerField(verbose_name='precio')),
                ('image', models.ImageField(upload_to='imagen', verbose_name='Imagen')),
            ],
        ),
    ]
