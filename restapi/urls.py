"""
URL configuration for restapi project.

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
from django.urls import path
from restapp import views
from restapp.views import ListblogAPIView, deleteblogAPIView
from restapp.views import CreateblogAPIView
from restapp.views import UpdateblogAPIView
from restapp.views import blogDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', ListblogAPIView.as_view()),
    path('single_data/<str:pk>/',blogDetailAPIView.as_view(),name='single_data'),
    path('create/',CreateblogAPIView.as_view(),name='create'),
    path('update/<str:pk>/',UpdateblogAPIView.as_view(),name='update'),
    path('delete/<str:pk>/',deleteblogAPIView.as_view(),name='delete'),
    path('todo', views.todo, name='todo'),
    path('todo_list',views.todo_list,name='todo_list'),

]

