# Job Portal

A full-stack Job Portal web application built using Django and PostgreSQL.

The platform connects Job Seekers and Recruiters in one application.

## Live Demo

https://jobportal-thjh.onrender.com/

## GitHub Repository

https://github.com/avinirkhe39/JobPortal

## Features

### Job Seeker

- User registration and login
- Browse available jobs
- Search jobs
- Filter jobs by location
- View complete job details
- View required experience
- View work mode
- View shift
- Apply for jobs
- Prevent duplicate job applications
- Track application status
- Manage profile
- Upload resume
- Dark / Light mode

### Recruiter

- Recruiter registration and login
- Recruiter dashboard
- Post new jobs
- Add required experience
- Select work mode
- Select shift
- Manage posted jobs
- View received applications
- Update application status

### Application Status

Recruiters can update applications as:

- Pending
- Shortlisted
- Rejected
- Selected

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- JavaScript
- Bootstrap
- PostgreSQL
- Git
- GitHub
- Render

## Project Structure

```text
JobPortal/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md