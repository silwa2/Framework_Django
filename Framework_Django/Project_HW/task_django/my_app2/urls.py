from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('cube/', views.cube, name='cube'),
    path('rand_num/', views.rand_num, name='rand_num'),
]
