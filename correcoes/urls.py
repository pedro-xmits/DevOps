from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import criar_correcao

urlpatterns = [
     path('', view= criar_correcao, name ="add-correcao"),
]