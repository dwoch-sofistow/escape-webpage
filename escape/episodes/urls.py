from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.episodemenu, name='episodemenu'),
    path('<int:Episode_id>/', views.detailep, name='blog'),
    path('<int:HiddenEpisode_id>/', views.hiddenepisode, name='blog'),
]
