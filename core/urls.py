from django.contrib import admin
from django.urls import path, include
from .views import addgasto, editar, listaGasto, deletar, gastoView, export_csv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view= listaGasto, name="gasto-view"),
    path('gasto/<int:id>', view= gastoView, name="gasto-view"),
    path('addgasto/', view= addgasto, name ="add-gasto"),
    path('editar/<int:id>', view= editar, name='editar'),
    path('deletar/<int:id>', view= deletar, name='deletar'),
    path('export_csv/', view= export_csv, name='export_csv'),
]

