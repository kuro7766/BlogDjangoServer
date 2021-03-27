"""blog_django_server URL Configuration

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
from django.contrib import admin
from django.urls import path
from pynat import url

from api import blog

urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^2280315050.*', functions.go),
    # url(r'^2280315050.*', functions.go),
    # url(r'^files.*', functions.files),
    # # url(r'test.*', functions2.test),
    # # path(r'tmp/ss', functions2.test),
    # path(r'qqrobotapi/2280315050/booklibrary', functions2.test),
    # path(r'myapi/2280315050', functions2.myapi),
    path(r'blog', blog.blog),
    # path(r'kmapi/files', functions3.file),
    # path(r'iptest', functions2.iptest),
]
