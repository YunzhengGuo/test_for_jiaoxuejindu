from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login',views.custom_login, name="login"),
    path('',views.custom_login, name="login"),
    path('custom_logout',views.custom_logout, name="custom_logout"),
    path('register',views.custom_register, name="register"),
    path('userprofile',views.update_userprofile, name="userprofile"),
]