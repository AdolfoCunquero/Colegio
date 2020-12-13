from django.forms import ModelForm
from core.models import Grado, Jornada
from django.forms.widgets import TextInput, Textarea, HiddenInput
from django.forms import ModelChoiceField

class GradoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control"
            form.field.widget.attrs['autocomplete']="off"

        self.fields["gr_nombre"].widget.attrs["autofocus"] = True
        self.fields['gr_estado'].widget = HiddenInput()
        self.fields['gr_usuario_creacion'].widget = HiddenInput()

    class Meta:
        model = Grado
        fields ="__all__"
        gr_id_jornada = ModelChoiceField(Jornada.objects.all())
        labels={
            "gr_id_jornada":"Jornada"
        }
        widgets={
            "gr_nombre":TextInput(attrs={"placeholder":"Ingrese el nombre del grado"}),
            "gr_descripcion":TextInput(attrs={"placeholder":"Ingrese una descripcion"}),
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