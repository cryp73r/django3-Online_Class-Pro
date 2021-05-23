from django.urls import path
from . import views

urlpatterns = [
    path('apiv1-ver-no-security-key-required/', views.apiv1Ver, name='apiv1Ver'),
]