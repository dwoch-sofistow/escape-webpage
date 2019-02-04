from django.urls import path

from . import views

urlpatterns = [
#    path('', views.home, name='home'),
    path('blogmenu/', views.blogmenu, name='blogmenu'),
    path('<int:blog_id>/', views.details, name='blog'),
    ]

from django.urls import path
