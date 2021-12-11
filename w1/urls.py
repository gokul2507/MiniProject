"""w1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('upload/',views.index,name="upload"),
    path('display/',views.display,name="display"),
    path('process/',views.process,name="processing"),
    path('sucess/',views.sucess,name="sucess"),
    path('excel/',views.excel,name="excel"),
    path('edit/', views.edit,name="edit"),
    path('delete/', views.delete,name="delete"),
    path('update/', views.update,name="update"),
    # path('display/',views.display,name="display"),
]
