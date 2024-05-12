# Generated by Django 5.0.4 on 2024-05-12 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_detallepedido_observaciones_alter_pedido_cliente'),
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='restaurante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurante.restaurante'),
            preserve_default=False,
        ),
    ]
