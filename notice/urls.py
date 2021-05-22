from django.urls import path, include
from . import views

urlpatterns = [
    path('apiv1-no-security-key-required/', views.notices, name='notices'),
]