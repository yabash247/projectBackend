from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', views.login_user, name='login_user'),
    path('LoginView/', views.LoginView, name='LoginView'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('dashboard/', views.dashboard, name='test'),
    path('profile/', views.UserProfile, name='profile'),
    path('updateProfile/', views.update_user_profile, name='update_user_profile'),
    path('changePassword/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('', views.getRoutes),
]

