from django.urls import path
from . import views


urlpatterns = [
    path('myProjects/', views.Projects, name='Projects'),
    path('Company/', views.Companies, name='Company'),
    path('activityNames/', views.ActivityName, name='activityNames'),
    path('ActivityNameById/', views.ActivityNameById, name='ActivityNameById'),
    path('Ponds/', views.Pond, name='Ponds'),
    path('fishSource/', views.fishSource, name='fishSource'),
    path('Stocks/', views.Stocks, name='Stocks'),
    path('Ponds/todo/', views.PondToDo, name='Ponds'),
    path('myPondsToDo/', views.myPondsToDo, name='myPondsToDo'),
    path('Fish/Sales/', views.Sale, name='Sales'),
    path('Stockings/', views.Stockings, name='Stockings'),
    path('Staff/', views.StaffData, name='Staff'),
    path('Project/', views.Projec, name='project'),
    path('test/', views.test.as_view(), name='test'),
    path('', views.getRoutes),
]

