from django.contrib import admin
from django.urls import path

from todolist.core.views import RegistrationView

urlpatterns = [
    path('core/signup', RegistrationView.as_view(), name="signup"),
]
