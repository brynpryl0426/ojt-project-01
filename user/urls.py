from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('update-employee/', views.update_employee, name ='update-employee'),
    path('employee-list/', views.employee_list, name ='employee-list'),
]
