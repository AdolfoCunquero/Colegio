from core.views.jornada.views import JornadaListView, JornadaCreateView, JornadaUpdateView, JornadaDeleteView
from core.views.grado.views import GradoListView, GradoCreateView, GradoUpdateView, GradoDeleteView
from core.views.curso.views import CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView
from core.views.horario.views import HorarioListView, HorarioCreateView, HorarioUpdateView, HorarioDeleteView
from django.urls import path

jornada_patterns=([
    path('list/',JornadaListView.as_view(), name="list"),
    path('create/',JornadaCreateView.as_view(), name="create"),
    path('update/<int:pk>/',JornadaUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/',JornadaDeleteView.as_view(), name="delete"),
],"jornada")

grado_patterns=([
    path('list/',GradoListView.as_view(), name="list"),
    path('create/',GradoCreateView.as_view(), name="create"),
    path('update/<int:pk>/',GradoUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/',GradoDeleteView.as_view(), name="delete"),
],"grado")

curso_patterns=([
    path('list/',CursoListView.as_view(), name="list"),
    path('create/',CursoCreateView.as_view(), name="create"),
    path('update/<int:pk>/',CursoUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/',CursoDeleteView.as_view(), name="delete"),
],"curso")

horario_patterns=([
    path('list/',HorarioListView.as_view(), name="list"),
    path('create/',HorarioCreateView.as_view(), name="create"),
    path('update/<int:pk>/',HorarioUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/',HorarioDeleteView.as_view(), name="delete"),
],"horario")