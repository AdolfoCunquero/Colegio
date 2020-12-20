from django.forms import ModelForm
from core.models import Curso
from django.forms.widgets import TextInput, Textarea, HiddenInput


class CursoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control form-control-sm" 
            form.field.widget.attrs['autocomplete']="off"

        self.fields["cu_nombre"].widget.attrs["autofocus"] = True

    class Meta:
        model = Curso
        fields =["cu_id_curso","cu_nombre","cu_descripcion"]
        widgets={
            "cu_nombre":TextInput(attrs={"placeholder":"Ingrese un nombre de curso"}),
            "cu_descripcion":TextInput(attrs={"placeholder":"Ingrese una descripcion"}),
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