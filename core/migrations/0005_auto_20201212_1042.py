# Generated by Django 3.1.3 on 2020-12-12 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_grado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grado',
            options={'ordering': ['gr_id_grado'], 'verbose_name': 'Grado', 'verbose_name_plural': 'Grados'},
        ),
        migrations.AlterModelTable(
            name='grado',
            table='grado',
        ),
    ]
