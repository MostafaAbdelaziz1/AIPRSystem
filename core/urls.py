from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .views import RoleBasedLoginView

urlpatterns = [
    path('login/', RoleBasedLoginView.as_view(), name='login'),
    path('register/', lambda request: redirect('login')),  # optional
    path('hod/home/', views.hod_home, name='hod_home'),
    path('student/home/', views.student_home, name='student_home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
]
