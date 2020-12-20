from django.forms import ModelForm
from core.models import Jornada
from django.forms.widgets import TextInput, Textarea


class JornadaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']="form-control form-control-sm"
            form.field.widget.attrs['autocomplete']="off"

        self.fields["jo_descripcion"].widget.attrs["autofocus"] = True
        

    class Meta:
        model = Jornada
        fields =["jo_id_jornada","jo_descripcion"]
        widgets={
            "jo_descripcion":TextInput(attrs={"placeholder":"Ingrese una descripcion"}),
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