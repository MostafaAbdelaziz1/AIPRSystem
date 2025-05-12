from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, "HOD"),
        (2, "Student"),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    session_start = models.DateField()
    session_end = models.DateField()
    cgpa = models.FloatField(default=0.0)
    completed_credit_hours = models.IntegerField(default=0)

class AcademicHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.CharField(max_length=20)
    grade = models.CharField(max_length=2)

class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50)  # Midterm/Final/Assignment
    marks = models.FloatField()


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # You can add custom fields if needed
    pass

from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    cgpa = models.FloatField()
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.user.username