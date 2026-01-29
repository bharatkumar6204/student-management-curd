"""
URL configuration for curdproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
admin.site.site_header = "Student Management System"
admin.site.site_title = "SMS Admin Panel"
admin.site.index_title = "CRUD Operations Dashboard"
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_std/', views.add_std, name='add_std'),
    path('delete-std/<int:roll>', views.delete_std, name='delete_std'),
    path('update-std/<int:roll>/', views.update_std, name='update_std'),
    path('do-update-std/<int:roll>/', views.do_update_std, name='do_update_std'),
   
    
    


    
]