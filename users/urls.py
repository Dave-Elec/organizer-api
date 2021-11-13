from django.urls import path, re_path, include
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
]
