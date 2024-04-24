"""
URL configuration for myservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views
from django.urls import path
from wildewidgets import WildewidgetDispatch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('hello/<slug:slug>', views.hello_name),
    path('hello1/', views.hello_with_params),
    path('form/', views.show_form),
    path('form/formdata/', views.show_form_data),
    path('wildewidgets_json', WildewidgetDispatch.as_view(), name='wildewidgets_json'),
    path("datatable/", views.TableView.as_view(), name="datatable"),
]
