from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import cadastro, listaUser, loginView, editar, deletar

urlpatterns = [
    path('', view= listaUser, name="user-view"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', view = cadastro, name='cadastro'),
    path('editar/<int:id>', view= editar, name='editar'),
    path('deletar/<int:id>', view= deletar, name='deletar'),
]