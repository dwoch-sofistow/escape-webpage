from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.episodemenu, name='episodes'),
    path('<int:episode_id>/', views.detailep, name='detailep'),
    path('<int:hiddenepisode_id>/', views.hiddenepisode, name='hiddenep'),
]
