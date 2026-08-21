from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.job_seeker_dashboard, name='job_seeker_dashboard'),
]