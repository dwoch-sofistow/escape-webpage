from django.urls import path

from blogs import views

urlpatterns = [
    path('', views.blogmenu, name='blogs'),
    path('<int:blog_id>/', views.blogdetail, name='blogdetail'),
    ]
