"""xiwang_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from book.views import *
from notes.views import *
from schedule.views import *
from signin.views import *
from webmark.views import *
from excerpt.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', book),
    path('api/notes/', notes),
    path('api/schedule/', schedule),
    path('api/signin/', signin),
    path('api/web/', webmark),
    path('api/excerpt/', excerpt),
]
