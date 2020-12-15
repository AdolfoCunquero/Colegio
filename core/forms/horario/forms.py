from django.forms import ModelForm
from core.models import Horario, Grado, Curso
from django.forms.widgets import TextInput, Textarea, HiddenInput, TimeInput, NumberInput
from django.forms import ModelChoiceField
from django import forms

class HorarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control"
            form.field.widget.attrs['autocomplete']="off"

        self.fields["ho_ciclo"].widget.attrs["autofocus"] = True
        self.fields['ho_estado'].widget = HiddenInput()
        self.fields['ho_usuario_creacion'].widget = HiddenInput()

    class Meta:
        model = Horario
        fields ="__all__"
        ho_id_curso = ModelChoiceField(Curso.objects.all())
        ho_id_grado = ModelChoiceField(Grado.objects.all())
        labels={
            "ho_id_curso":"Curso",
            "ho_id_grado":"Grado"
        }

        ho_hora_inicio = forms.TimeField(input_formats=['%H:%M','%I:%M %p'],
                      widget=forms.TimeInput(attrs={'size':'8','class':'time_field'},format=["%H:%M","%I:%M %p"]))

        widgets={
            "ho_ciclo":TextInput(attrs={"placeholder":"Ingrese el ciclo"}),
            "ho_usuario_catedratico":TextInput(attrs={"placeholder":"Ingrese el catedratico"}),
            "ho_no_periodo":NumberInput(attrs={"placeholder":"Ingrese el no. de periodo"}),
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