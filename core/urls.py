from django.urls import path, include
from . import views

app_name= 'tree'
urlpatterns = [
    path('', views.treeHome, name='home'),
    path('<int:pk>', views.treeDetail, name='detail'),
]