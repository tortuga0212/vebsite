from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'start'),
    path('about-us', views.about, name = 'about'),
    path('home', views.home, name = 'home'),
]