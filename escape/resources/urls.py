from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.resourcemenu, name='resources'),
    path('<int:Resource_id>/', views.detailres, name='detailres'),
]
# Schemat przejść:
#   home, navbar => resourcemenu
#   resourcemenu => detailres
