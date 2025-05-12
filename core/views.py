from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.urls import reverse

class RoleBasedLoginView(LoginView):
    template_name = 'core/login.html'

    def get_success_url(self):
        return redirect_user(self.request.user)

def redirect_user(user):
    if user.user_type == 1:  # HOD
        return reverse('hod_home')
    elif user.user_type == 2:  # Student
        return reverse('student_home')
    return reverse('login')  # fallback

def login_redirect_view(request):
    if request.user.user_type == 1:
        return redirect('hod_home')
    elif request.user.user_type == 2:
        return redirect('student_home')
    else:
        return redirect('login')  # fallback

def hod_home(request):
    return render(request, 'core/hhome.html')

def student_home(request):
    return render(request, 'core/shome.html')


from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    # Assuming the user is a student, retrieve their data.
    student = request.user

    # Optionally, if you have a model for additional student information:
    # student_profile = StudentProfile.objects.get(user=student)

    context = {
        'student': student,
        # 'student_profile': student_profile, # If you have a student profile model
    }

    return render(request, 'core/dashboard.html', context)


from django.contrib.auth.decorators import login_required
from .models import StudentProfile


@login_required
def student_dashboard(request):
    student = request.user
    try:
        student_profile = StudentProfile.objects.get(user=student)
    except StudentProfile.DoesNotExist:
        student_profile = None

    context = {
        'student': student,
        'student_profile': student_profile,
    }

    return render(request, 'core/dashboard.html', context)

import joblib
import os
from django.conf import settings
from django.shortcuts import render
from .models import Student

def recommend_schedule(request):
    student = request.user.student
    model_path = os.path.join(settings.BASE_DIR, 'core/ai/schedule_model.pkl')
    model = joblib.load(model_path)

    # Input: dummy example based on your model
    input_data = [[student.cgpa, student.completed_credit_hours]]
    recommended_subject_ids = model.predict(input_data)[0]  # assuming it returns subject IDs

    from .models import Subject
    subjects = Subject.objects.filter(id__in=recommended_subject_ids)

    return render(request, 'student/recommendation.html', {'subjects': subjects})
