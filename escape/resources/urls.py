from django.urls import path

from . import views

urlpatterns = [
    path(' ', views.resourcemenu, name='resourcemenu'),
    path('<int:Resource_id>/', views.detailres, name='resource'),
    path('<int:HiddenResource_id>/', views.hiddenresource, name='hiddenresource'),
]
