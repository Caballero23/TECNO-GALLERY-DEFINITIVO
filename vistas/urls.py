
from django.urls import path


from vistas.views import agregar_producto,SearchResultsListView ,modificar,eliminar,añadir


urlpatterns = [

    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('buscamoviles/', SearchResultsListView.as_view() ,name="buscamoviles"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('añadir/', añadir, name="añadir"),
]