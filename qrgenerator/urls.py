from django.urls import path
from . import views

urlpatterns = [
    path('', views.qrGenerator, name='qr_generator'),
]