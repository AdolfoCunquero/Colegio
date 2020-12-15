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

class Curso(models.Model):
    cu_id_curso = models.AutoField( primary_key=True, verbose_name="ID Curso")
    cu_nombre = models.CharField(max_length=150, blank=False, null=False, verbose_name="Nombre")
    cu_descripcion = models.CharField(max_length=500, blank=True, null=True, verbose_name="Descripcion")
    cu_estado = models.BooleanField(default=True, verbose_name="Estado", null=False)
    cu_fecha_creacion = models.DateField(auto_now_add= True, verbose_name='Fecha creacion')
    cu_usuario_creacion = models.CharField(default="", max_length=50, blank=True, null=True,  verbose_name="Usuario creacion")
    
    class Meta():
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['cu_id_curso']
        db_table ="curso"

    def to_json(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.cu_nombre

class Horario(models.Model):
    ho_id_grado_curso = models.AutoField( primary_key=True, verbose_name="ID")   
    ho_ciclo = models.CharField(max_length=4, blank=False, null=False, verbose_name="Ciclo") 
    ho_id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    ho_id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ho_usuario_catedratico = models.CharField(max_length=50, blank=True, null=True, verbose_name="Catedratico")
    ho_hora_inicio = models.TimeField(blank=False, null=False, verbose_name="Hora inicio")
    ho_hora_fin = models.TimeField(blank=False, null=False, verbose_name="Hora fin")
    ho_no_periodo = models.IntegerField(blank=False, null=False, verbose_name="No Periodo")
    ho_estado = models.BooleanField(default=True, verbose_name="Estado", null=False)
    ho_fecha_creacion = models.DateField(auto_now_add= True, verbose_name='Fecha creacion')
    ho_usuario_creacion = models.CharField(default="", max_length=50, blank=True, null=True,  verbose_name="Usuario creacion")

    class Meta():
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['ho_id_grado_curso']
        db_table ="horario"
        unique_together = (('ho_ciclo', 'ho_id_grado','ho_id_curso'))

    def to_json(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.ho_ciclo + " - " + str(self.ho_id_grado) + " - " + str(self.ho_id_curso)