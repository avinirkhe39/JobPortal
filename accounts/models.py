from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User Model
# This model stores Job Seeker and Recruiter users
class User(AbstractUser):

    # User Role Options
    # job_seeker = person who searches and applies for jobs
    # recruiter = person who posts jobs
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    # Stores the role of the user
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='job_seeker'
    )

    # Profile Information
    phone = models.CharField(
        max_length=15,
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    education = models.TextField(
        blank=True
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    # Shows username when we display User object
    def __str__(self):
        return self.username


# Job Model
# This model stores information about jobs posted by recruiters
class Job(models.Model):

    # Job title
    # Example: Python Developer
    title = models.CharField(max_length=200)

    # Company name
    # Example: TCS, Infosys
    company = models.CharField(max_length=200)

    # Job location
    # Example: Pune, Mumbai
    location = models.CharField(max_length=100)

    # Required experience for the job
    # Example: Fresher, 1-2 Years, 3-5 Years
    experience = models.CharField(
    max_length=50,
    default='Fresher'
    )

    # Work Mode
    MODE_CHOICES = (
        ('onsite', 'On-site'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    )

    mode = models.CharField(
        max_length=20,
        choices=MODE_CHOICES,
        default='onsite'
    )

    # Work Shift
    SHIFT_CHOICES = (
        ('day', 'Day Shift'),
        ('night', 'Night Shift'),
    )

    shift = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES,
        default='day'
    )

    # Complete information about the job
    description = models.TextField()

    # Salary offered for the job
    # blank=True means salary is optional
    salary = models.CharField(max_length=100, blank=True)

    # Automatically stores the date and time
    # when the job is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Connects the Job with the Recruiter who posted it
    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posted_jobs'
    )

    # Shows Job title when we display Job object
    def __str__(self):
        return self.title

# Application Model
# This model stores job applications submitted by Job Seekers
class Application(models.Model):

    # The Job Seeker who is applying
    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    # The job for which the user is applying
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    # Date and time when the application was submitted
    applied_at = models.DateTimeField(auto_now_add=True)

    # Application status
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('selected', 'Selected'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    class Meta:
    # One Job Seeker can apply only once for the same job
        constraints = [
            models.UniqueConstraint(
                fields=['applicant', 'job'],
                name='unique_job_application'
            )
        ]

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"    