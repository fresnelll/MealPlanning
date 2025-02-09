from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_meals, name='search_meals'),
    path('saved-meals/', views.saved_meals, name='saved_meals'),
    path('save-meal/', views.save_meal, name='save_meal'),
    path('signup/', views.signup, name='signup'),
    path('delete-meal/<int:meal_id>/', views.delete_meal, name='delete_meal'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
