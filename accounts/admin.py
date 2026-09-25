from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Job, Application


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Job Portal Information', {
            'fields': ('role',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Job Portal Information', {
            'fields': ('role',)
        }),
    )

# Register Job model in Django Admin
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    # Fields displayed in the Job list
    list_display = (
        'title',
        'company',
        'location',
        'salary',
        'recruiter',
        'created_at',
    )

    # Fields that can be searched
    search_fields = (
        'title',
        'company',
        'location',
    )

    # Filters available in Admin
    list_filter = (
        'location',
        'created_at',
    )    

# Register Application model in Django Admin
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    # Fields displayed in Application list
    list_display = (
        'applicant',
        'job',
        'status',
        'applied_at',
    )

    # Search applications by username or job title
    search_fields = (
        'applicant__username',
        'job__title',
    )

    # Filter applications by status and date
    list_filter = (
        'status',
        'applied_at',
    )    