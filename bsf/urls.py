from django.urls import path
from . import views

urlpatterns = [
   path('', views.getRoutes),
   path('batch', views.Batchs, name='batch'),
   path('net', views.Nets, name='net'),
   path('laying', views.Lays, name='laying'),

]