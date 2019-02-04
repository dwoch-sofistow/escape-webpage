from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.resourcemenu, name='resources'),
    path('<int:Resource_id>/', views.detailres, name='detailres'),
    path('<int:HiddenResource_id>/', views.hiddenresource, name='hiddenresource'),
]
