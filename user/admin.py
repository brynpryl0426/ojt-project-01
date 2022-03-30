from django.contrib import admin
from .models import Department, JobRole, Employee

# Register your models here.
admin.site.register(Department)
admin.site.register(JobRole)
admin.site.register(Employee)