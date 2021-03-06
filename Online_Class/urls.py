"""Online_Class URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from quizExam.views import QuizSchedule
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from classdetail import views
# import quizExam

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupusr, name='signupusr'),
    path('login/', views.loginusr, name='loginusr'),
    path('logout/', views.logoutusr, name='logoutusr'),
    path('changepassword/', views.chnpsw, name='chnpsw'),

    # Display
    path('current/', views.currentusr, name='currentusr'),

    # API
    path('apiv1-no-security-key-required/', views.apiv1CS, name='apiv1CS'),
    path('apiv1-it-no-security-key-required/', views.apiv1IT, name='apiv1IT'),
    path('apiv1-ver-no-security-key-required/', views.apiv1Ver, name='apiv1IT'),

    # API Notice
    path('notice/', include('notice.urls')),

    #API AppRelease
    path('app/', include('appRelease.urls')),

    # path('quiz/', quizExam.views.QuizSchedule, name='QuizSchedule'),

    re_path(r'^app/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)