from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.episodemenu, name='episodes'),
    path('<int:episode_id>/', views.detailep, name='detailep'),
    path('hiddenresource <int:hiddenresource_id>/', views.hiddenresource, name='hiddenresource'),

]

# Schemat przejść:
#   home, navbar => episodemenu
#   episodemenu => detailep
#   detailep => hiddenresource
