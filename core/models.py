from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from colegio.settings import MEDIA_URL, STATIC_URL

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
    gr_id_jornada = models.ForeignKey(Jornada, on_delete=models.PROTECT, db_column="gr_id_jornada", related_name="grado_jornada", verbose_name="Jornada")
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

class Ciclo(models.Model):
    ci_ciclo = models.CharField(max_length=10, primary_key=True, verbose_name="Ciclo")
    ci_fecha_inicio = models.DateField(null=False, verbose_name="Fecha inicio")
    ci_fecha_fin = models.DateField(null=False, verbose_name="Fecha Fin")
    ci_estado = models.BooleanField(default=False, null=False, blank=False, verbose_name="Estado")
    ci_fecha_creacion = models.DateField(auto_now_add= True, verbose_name='Fecha creacion')
    ci_usuario_creacion = models.CharField(default=settings.AUTH_USER_MODEL, max_length=50,  verbose_name="Usuario creacion")

    class Meta():
        verbose_name = 'Ciclo'
        verbose_name_plural = 'Ciclos'
        ordering = ['ci_ciclo']
        db_table ="ciclo"

    def to_json(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.ci_ciclo 


class Horario(models.Model):
    ho_id_grado_curso = models.AutoField( primary_key=True, verbose_name="ID")   
    ho_ciclo = models.ForeignKey(Ciclo, on_delete = models.PROTECT, db_column="ho_ciclo", related_name="horario_ciclo", verbose_name="Ciclo") 
    ho_id_grado = models.ForeignKey(Grado, on_delete=models.PROTECT, db_column="ho_id_grado", related_name="horario_grado", verbose_name="Grado")
    ho_id_curso = models.ForeignKey(Curso, on_delete=models.PROTECT, db_column="ho_id_curso", related_name="horario_curso", verbose_name="Curso")
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
        unique_together = ['ho_ciclo', 'ho_id_grado','ho_id_curso']

    def to_json(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str(self.ho_ciclo) + " - " + str(self.ho_id_grado) + " - " + str(self.ho_id_curso)

    def delete(self):
        self.ho_estado = False
        self.save()



# class Usuario(AbstractUser):
#     image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
#     token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    
#     def get_image(self):
#         if self.image:
#             return '{}{}'.format(MEDIA_URL, self.image)
#         return '{}{}'.format(STATIC_URL, 'img/empty.png')

#     def toJSON(self):
#         item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
#         if self.last_login:
#             item['last_login'] = self.last_login.strftime('%Y-%m-%d')
#         item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
#         item['image'] = self.get_image()
#         item['full_name'] = self.get_full_name()
#         item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
#         return item

#     def get_group_session(self):
#         try:
#             request = get_current_request()
#             groups = self.groups.all()
#             if groups.exists():
#                 if 'group' not in request.session:
#                     request.session['group'] = groups[0]
#         except:
#             pass
#     fecha_nacimiento = models.DateField(null=True,  verbose_name="Fecha nacimiento")

        