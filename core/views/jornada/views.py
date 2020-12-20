from django.shortcuts import redirect, render
from core.models import Jornada
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from core.forms.jornada.forms import JornadaForm
from django.urls import reverse_lazy

class JornadaListView(ListView):
    model = Jornada
    form_class = JornadaForm
    template_name = "jornada/list.html"

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Jornada.objects.filter(jo_estado=True):
                    data.append(i.to_json())
            else:
                data["error"] = "Ha ocurrido un error"
            
        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["create_url"] = reverse_lazy("jornada:create")
        context["title"] = 'Listado de jornadas'
        return context

class JornadaCreateView(CreateView):
    model = Jornada
    form_class = JornadaForm
    template_name = "crud/form.html"
    success_url = reverse_lazy("jornada:list")

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = self.get_form()#CategoryForm(request.POST))
            print(form)
            data = form.save()

        except Exception as e:
            data["error"] = str(e)
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["list_url"] = reverse_lazy("jornada:list")
        context["title"] = 'Crear jornada'
        return context

    
class JornadaUpdateView(UpdateView):
    model = Jornada
    form_class = JornadaForm
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
        context["list_url"] = reverse_lazy("jornada:list")
        context["title"] = 'Modificar jornada'
        return context


class JornadaDeleteView(DeleteView):
    model = Jornada
    form_class = JornadaForm
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
        context["list_url"] = reverse_lazy("jornada:list")
        context["title"] = 'Eliminar jornada'
        context["item"] = self.object.__str__()
        return context

   