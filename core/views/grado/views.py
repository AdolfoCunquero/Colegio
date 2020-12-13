from django.shortcuts import redirect, render
from core.models import Grado, Jornada
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from core.forms.grado.forms import GradoForm
from django.urls import reverse_lazy

class GradoListView(ListView):
    model = Grado
    form_class = GradoForm
    template_name = "grado/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            data = []
            if action == 'searchdata':
                for i in Grado.objects.all():
                    grado = i.to_json()
                    jornada = Jornada.objects.filter(jo_id_jornada = i.to_json()["gr_id_jornada"])
                    grado["jornada"] = jornada[0].jo_descripcion
                    data.append(grado)
                    
            else:
                data["error"] = "Ha ocurrido un error"
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["create_url"] = reverse_lazy("grado:create")
        context["list_url"] = reverse_lazy("grado:list")
        context["entity"] = 'Grado'
        context["title"] = 'Lista de Grados'
        return context

class GradoCreateView(CreateView):
    model = Grado
    form_class = GradoForm
    template_name = "crud/form.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "add":
                form = self.get_form()#CategoryForm(request.POST))
                data = form.save()

            else:
                data["No es una opcion valida"]
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["list_url"] = reverse_lazy("grado:list")
        context["entity"] = 'Grado'
        context["title"] = 'Crear grado'
        return context

    
class GradoUpdateView(UpdateView):
    model = Grado
    form_class = GradoForm
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
        context["list_url"] = reverse_lazy("grado:list")
        context["entity"] = 'Grado'
        context["title"] = 'Modificar grado'
        return context


class GradoDeleteView(DeleteView):
    model = Grado
    form_class = GradoForm
    template_name = "crud/delete.html"
    success_url = reverse_lazy("grado:list")
    
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
        context["list_url"] = reverse_lazy("grado:list")
        context["entity"] = 'Grado'
        context["title"] = 'Eliminar grado'
        context["item"] = self.object.__str__()
        return context

   