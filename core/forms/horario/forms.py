from django.forms import ModelForm
from core.models import Horario, Grado, Curso, Ciclo
from django.forms.widgets import TextInput, Textarea, HiddenInput, TimeInput, NumberInput
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

class HorarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control form-control-sm"
            form.field.widget.attrs['autocomplete']="off"

        self.fields["ho_ciclo"].widget.attrs["autofocus"] = True
        self.fields["ho_ciclo"].queryset = Ciclo.objects.filter(ci_estado=True)
        self.fields["ho_id_curso"].queryset = Curso.objects.filter(cu_estado=True)
        self.fields["ho_id_grado"].queryset = Grado.objects.filter(gr_estado=True)
        

    class Meta:
        model = Horario
        fields =["ho_id_grado_curso","ho_ciclo","ho_id_grado","ho_id_curso","ho_usuario_catedratico","ho_hora_inicio","ho_hora_fin","ho_no_periodo"]
        
        widgets={
            "ho_ciclo": forms.Select(),
            "ho_id_curso": forms.Select(),
            "ho_id_grado": forms.Select(),
            "ho_usuario_catedratico":TextInput(attrs={"placeholder":"Ingrese el catedratico"}),
            "ho_no_periodo":NumberInput(attrs={"placeholder":"Ingrese el no. de periodo"}),
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "El horario ya existe",
            }
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            
            else:
                data["error"] = form.errors

        except Exception as e:
            data["error"] = str(e)

        return data