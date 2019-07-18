"""Gmail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from voicemail.views import home,LoginView,LogoutView,RegisterView,password,main,base,send_email
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name="home" ),
    path('base/',base, name="base"),
    path('login/',LoginView, name="login"),
    path('logout/',LogoutView, name="logout"),
    path('password/',password, name="password"),
    path('main/',main, name="main"),
    path('compose/',send_email, name="compose"),
    path('register/', RegisterView, name="register"),
    # path('sendemail/', sendemail, name="sendemail"),

]
