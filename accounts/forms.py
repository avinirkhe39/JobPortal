from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Job


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'role',
            'password1',
            'password2',
        ]


# Form used by recruiters to create a new job
class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            'title',
            'company',
            'location',
            'experience',
            'mode',
            'shift',
            'description',
            'salary',
        ]

# Form used by users to edit their profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'skills',
            'education',
            'resume',
        ]        