from django.shortcuts import redirect, render
from core.models import Grado, Curso, Horario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from core.forms.horario.forms import HorarioForm
from django.urls import reverse_lazy

class HorarioListView(ListView):
    model = Horario
    form_class = HorarioForm
    template_name = "horario/list.html"

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            data = []
            if action == 'searchdata':
                for i in Horario.objects.filter(ho_estado=True):
                    horario = i.to_json()
                    curso = Curso.objects.filter( cu_id_curso = i.to_json()["ho_id_curso"])
                    grado = Grado.objects.filter( gr_id_grado = i.to_json()["ho_id_grado"])
                    horario["curso"] = curso[0].cu_nombre
                    horario["grado"] = grado[0].gr_nombre
                    data.append(horario)
                    
            else:
                data["error"] = "Ha ocurrido un error"
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["create_url"] = reverse_lazy("horario:create")
        context["title"] = 'Lista de Horarios'
        return context

class HorarioCreateView(CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = "crud/form.html"

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()#CategoryForm(request.POST))
            data = form.save()
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["list_url"] = reverse_lazy("horario:list")
        context["title"] = 'Crear Horario'
        return context

    
class HorarioUpdateView(UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = "crud/form.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()#CategoryForm(request.POST)
            data = form.save()
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["list_url"] = reverse_lazy("horario:list")
        context["title"] = 'Modificar Horario'
        return context


class HorarioDeleteView(DeleteView):
    model = Horario
    form_class = HorarioForm()
    template_name = "crud/delete.html"


    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data)

    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["list_url"] = reverse_lazy("horario:list")
        context["title"] = 'Eliminar horario'
        context["item"] = self.object.__str__()
        return context

   