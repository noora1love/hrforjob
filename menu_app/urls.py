from django.urls import path
from menu_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
