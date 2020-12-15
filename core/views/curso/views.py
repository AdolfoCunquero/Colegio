from django.shortcuts import redirect, render
from core.models import Curso
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from core.forms.curso.forms import  CursoForm
from django.urls import reverse_lazy

class CursoListView(ListView):
    model = Curso
    form_class = CursoForm
    template_name = "curso/list.html"

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Curso.objects.all():
                    data.append(i.to_json())
            else:
                data["error"] = "Ha ocurrido un error"
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["create_url"] = reverse_lazy("curso:create")
        context["list_url"] = reverse_lazy("curso:list")
        context["entity"] = 'Curso'
        context["title"] = 'Listado de cursos'
        return context

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "crud/form.html"
    success_url = reverse_lazy("curso:list")

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
        context["list_url"] = reverse_lazy("curso:list")
        context["entity"] = 'Curso'
        context["title"] = 'Crear curso'
        return context

    
class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
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
        context["list_url"] = reverse_lazy("curso:list")
        context["entity"] = 'Curso'
        context["title"] = 'Modificar curso'
        return context


class CursoDeleteView(DeleteView):
    model = Curso
    form_class = CursoForm
    template_name = "crud/delete.html"
    success_url = reverse_lazy("curso:list")
    
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
        context["list_url"] = reverse_lazy("curso:list")
        context["entity"] = 'Curso'
        context["title"] = 'Eliminar curso'
        context["item"] = self.object.__str__()
        return context

   