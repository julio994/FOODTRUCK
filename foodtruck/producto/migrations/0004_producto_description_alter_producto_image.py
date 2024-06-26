# Generated by Django 5.0.4 on 2024-04-16 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("producto", "0003_producto_id_restaurante"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="description",
            field=models.TextField(default="", verbose_name="descripcion"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="producto",
            name="image",
            field=models.ImageField(upload_to="producto", verbose_name="Imagen"),
        ),
    ]
