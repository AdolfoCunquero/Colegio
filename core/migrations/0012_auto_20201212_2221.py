# Generated by Django 3.1.3 on 2020-12-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cu_descripcion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion'),
        ),
    ]