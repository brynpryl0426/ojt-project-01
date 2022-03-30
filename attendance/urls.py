from django.urls import path, include
from . import views

urlpatterns = [
    path('employee-logs/', views.employee_logs, name ='employee-logs'),
]
