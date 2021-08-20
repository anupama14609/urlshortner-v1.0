from django.urls import path
from .views import home, Create, Go

urlpatterns = [ 
    path('', home, name="home"),
    path('create', Create, name='create'),
    path('<str:pk>', Go, name='go')

]