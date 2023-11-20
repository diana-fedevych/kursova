from django.urls import path
from . import views
from .views import index, about, generate_text

urlpatterns = [
   path('', views.index, name='home'),
   path('about', views.about, name='about'),
   path('generate_text/', generate_text, name='generate_text'),
]
