from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib import messages

from .forms import RegistrationForm, JobForm, ProfileForm
from .models import Job, Application

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'job_seeker':
                return redirect('job_seeker_dashboard')

            elif user.role == 'recruiter':
                return redirect('recruiter_dashboard')
            
        messages.error(request, "Invalid username or password.")
        return redirect('login')
        

    return render(request, 'accounts/login.html')

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def job_seeker_dashboard(request):

    if request.user.role != "job_seeker":
        return redirect("recruiter_dashboard")

    jobs = Job.objects.all().order_by('-created_at')

    search_query = request.GET.get('search', '').strip()

    if search_query:
        jobs = jobs.filter(
            models.Q(title__icontains=search_query) |
            models.Q(company__icontains=search_query) |
            models.Q(description__icontains=search_query)
        )

    location = request.GET.get('location', '').strip()

    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    applied_job_ids = Application.objects.filter(
        applicant=request.user
    ).values_list('job_id', flat=True)

    return render(
        request,
        'accounts/job_seeker_dashboard.html',
        {
            'jobs': jobs,
            'applied_job_ids': applied_job_ids,
            'search_query': search_query,
            'location': location,
        }
    )

# Recruiter Dashboard
# Shows the dashboard only to logged-in recruiters
@login_required
def recruiter_dashboard(request):

    if request.user.role != "recruiter":
        return redirect("job_seeker_dashboard")

    jobs = Job.objects.filter(
        recruiter=request.user
    ).order_by('-created_at')

    return render(
        request,
        'accounts/recruiter_dashboard.html',
        {'jobs': jobs}
    )

# Post New Job
# Allows a logged-in recruiter to create a new job
@login_required
def post_job(request):

    if request.user.role != "recruiter":
        return redirect("job_seeker_dashboard")

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():

            # Create job object but don't save yet
            job = form.save(commit=False)

            # Automatically assign the logged-in recruiter
            job.recruiter = request.user

            # Save job to database
            job.save()

            # Go back to recruiter dashboard
            return redirect('recruiter_dashboard')

    else:
        form = JobForm()

    return render(
        request,
        'accounts/post_job.html',
        {'form': form}
    )

# View Applications
# Shows applications received for jobs posted by the logged-in recruiter
@login_required
def view_applications(request, job_id):

    # Get the selected job
    job = get_object_or_404(Job,
        id=job_id,
        recruiter=request.user
    )

    # Get applications for this job
    applications = Application.objects.filter(
        job=job
    ).order_by('-applied_at')

    return render(
        request,
        'accounts/view_applications.html',
        {
            'job': job,
            'applications': applications,
        }
    )

# Apply for a Job
# This view creates an application for the logged-in Job Seeker
@login_required
def apply_job(request, job_id):

    if request.user.role != "job_seeker":
        return redirect("recruiter_dashboard")

    # Get the selected job
    job = Job.objects.get(id=job_id)

    # Check if the user has already applied for this job
    already_applied = Application.objects.filter(
        applicant=request.user,
        job=job
    ).exists()

    # If already applied, show a message
    if already_applied:
        return render(
            request,
            'accounts/already_applied.html',
            {'job': job}
        )

    # Create a new application
    Application.objects.create(
        applicant=request.user,
        job=job
    )

    # Go back to dashboard
    return redirect('job_seeker_dashboard')

# My Applications
# Shows all jobs applied by the logged-in Job Seeker
@login_required
def my_applications(request):

    if request.user.role != "job_seeker":
        return redirect("recruiter_dashboard")

    # Get applications of the logged-in user
    applications = Application.objects.filter(
        applicant=request.user
    ).order_by('-applied_at')

    return render(
        request,
        'accounts/my_applications.html',
        {'applications': applications}
    )

# Update Application Status
@login_required
def update_application_status(request, application_id):

    if request.user.role != "recruiter":
        return redirect("job_seeker_dashboard")

    if request.method == 'POST':
        application = Application.objects.get(
            id=application_id,
            job__recruiter=request.user
        )

        new_status = request.POST.get('status')

        if new_status in ['pending', 'shortlisted', 'rejected', 'selected']:
            application.status = new_status
            application.save()

        return redirect(
            'view_applications',
            job_id=application.job.id
        )

    return redirect("recruiter_dashboard")

# My Profile
@login_required
def my_profile(request):

    if request.method == 'POST':

        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('my_profile')

    else:

        form = ProfileForm(
            instance=request.user
        )

    return render(
        request,
        'accounts/my_profile.html',
        {'form': form}
    )

# Job Details
@login_required
def job_details(request, job_id):

    job = Job.objects.get(id=job_id)

    return render(
        request,
        'accounts/job_details.html',
        {'job': job}
    )

# Logout
@login_required
def user_logout(request):

    logout(request)

    return redirect('login')