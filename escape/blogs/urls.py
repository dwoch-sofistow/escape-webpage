from django.urls import path

from blogs import views

urlpatterns = [
    path('blogmenu/', views.blogmenu, name='blogmenu'),
    path('<int:blog_id>/', views.details, name='blog'),
    ]
