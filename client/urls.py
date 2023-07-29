from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage , name='homepage'),
    path('register/', views.tenantRegistration , name='register'),
]