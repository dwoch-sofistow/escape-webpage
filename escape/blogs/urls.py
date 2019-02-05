from django.urls import path

from blogs import views

urlpatterns = [
    # główne menu bloga
    path('', views.blogmenu, name='blogs'),
    # pojedyncze wpisy
    path('<int:blog_id>/', views.blogdetail, name='blogdetail'),
    # ukryte odcinki
    path('hiddenepisode <int:hiddenepisode_id>', views.hiddenepisode, name='hiddenepisode')
    ]

# Schemat przejść:
#   home, navbar => blogmenu
#   blogmenu => blogdetail 
#   blogdetail => hiddenepisode
