from core.views.jornada.views import JornadaListView, JornadaCreateView, JornadaUpdateView, JornadaDeleteView
from core.views.grado.views import GradoListView, GradoCreateView, GradoUpdateView, GradoDeleteView
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