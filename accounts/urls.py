from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.job_seeker_dashboard, name='job_seeker_dashboard'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('recruiter-dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('post-job/', views.post_job, name='post_job'),
    path(
    'view-applications/<int:job_id>/',
    views.view_applications,
    name='view_applications'
),
path(
    'update-application-status/<int:application_id>/',
    views.update_application_status,
    name='update_application_status'
),
path(
    'my-profile/',
    views.my_profile,
    name='my_profile'
),
path(
    'job-details/<int:job_id>/',
    views.job_details,
    name='job_details'
),
path(
    'logout/',
    views.user_logout,
    name='logout'
),
]