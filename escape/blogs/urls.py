from django.urls import path

from blogs import views

urlpatterns = [
    path('', views.blogmenu, name='blogs'),
    path('<int:blog_id>/', views.blogdetail, name='blogdetail'),
    path('hiddenepisode <int:hiddenepisode_id>', views.hiddenepisode, name='hiddenepisode')
    ]
