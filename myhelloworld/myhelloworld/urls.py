from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('count/',views.count,name='count'), 
    path('home/', views.home,name='home')
]
