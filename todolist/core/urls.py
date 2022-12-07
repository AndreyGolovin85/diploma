from django.urls import path

from . import views

urlpatterns = [
    path('core/signup', views.RegistrationView.as_view(), name='signup'),
    path('core/login', views.LoginView.as_view(), name='login'),
    path('core/profile', views.ProfileView.as_view(), name='profile'),
    path('core/update_password', views.PasswordUpdateView.as_view(), name='update_password'),
]
