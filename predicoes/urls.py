from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import exportar_gastos_csv

urlpatterns = [
    path('exportar-gastos-csv/', view=exportar_gastos_csv, name='exportar_gastos_csv'),
]