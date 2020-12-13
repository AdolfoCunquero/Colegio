from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from django.contrib import admin

class Jornada(models.Model):
    jo_id_jornada = models.AutoField( primary_key=True, verbose_name="ID Jornada")
    jo_descripcion = models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name="Descripcion")
    jo_estado = models.BooleanField(default=True, verbose_name="Estado", null=False)
    jo_fecha_creacion = models.DateField(auto_now_add= True, verbose_name='Fecha creacion')
    jo_usuario_creacion = models.CharField(max_length=50, blank=True, null=True, verbose_name="Usuario creacion")

    class Meta():
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
        ordering = ['jo_id_jornada']
        db_table ="jornada"

    def to_json(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.jo_descripcion

class Grado(models.Model):
    gr_id_grado = models.AutoField( primary_key=True, verbose_name="ID Grado")
    gr_nombre = models.CharField(max_length=50, blank=False, null=False, verbose_name="Nombre")
    gr_descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Descripcion")
    gr_id_jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    gr_estado = models.BooleanField(default=True, verbose_name="Estado", null=False)
    gr_fecha_creacion = models.DateField(auto_now_add= True, verbose_name='Fecha creacion')
    gr_usuario_creacion = models.CharField(default="", max_length=50, blank=True, null=True,  verbose_name="Usuario creacion")

    class Meta():
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        ordering = ['gr_id_grado']
        db_table ="grado"

    def to_json(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.gr_nombre

