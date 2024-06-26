# Generated by Django 5.0.4 on 2024-04-16 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("producto", "0002_producto_created_producto_updated"),
        ("restaurante", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="id_restaurante",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="restaurante.restaurante",
                verbose_name="Restaurante",
            ),
            preserve_default=False,
        ),
    ]
