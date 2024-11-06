from django.urls import path
from . import views

urlpatterns = [
   path('', views.getRoutes),
   path('Authorities', views.Authorities, name='Authorities'),
   path('StaffCurrents', views.StaffCurrents, name='StaffCurrents'),
   path('StaffOrgCharts', views.StaffOrgCharts, name='StaffOrgCharts'),
   path('batch', views.Batchs, name='batch'),
   path('net', views.Nets, name='net'),
   path('NetStatus', views.NetStatus, name='NetStatus'),
   path('Containers', views.Containers, name='Containers'),
   path('ContainerStatus', views.ContainerStats, name='ContainerStatus'),

]