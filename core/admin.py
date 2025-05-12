from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(StudentResult)
admin.site.register(AcademicHistory)
