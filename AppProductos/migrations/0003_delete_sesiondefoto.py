# Generated by Django 4.2.16 on 2024-12-09 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProductos', '0002_sesiondefoto_alter_sesionfotografica_activo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SesionDeFoto',
        ),
    ]
