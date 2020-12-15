# Generated by Django 3.1.3 on 2020-12-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201212_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('cu_id_curso', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Curso')),
                ('cu_nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('cu_descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('cu_estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('cu_fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('cu_usuario_creacion', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Usuario creacion')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'curso',
                'ordering': ['cu_id_curso'],
            },
        ),
    ]