from django.contrib import admin
from django.urls import path, include
from .views import listaDesp, addDesp, despView, editDesp, deletDesp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view= listaDesp, name="desp-view"),
    path('addDesp/', view= addDesp, name ="add-desp"),
    path('despesa/<int:id>', view= despView, name="despesa-view"),
    path('editar/<int:id>', view= editDesp, name='editar'),
    path('deletar/<int:id>', view= deletDesp, name='deletar'),
]