from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('update-employee/<int:user_id>', views.update_employee, name ='update-employee'),
    path('employee-list/', views.employee_list, name ='employee-list'),
    path('download-data/', views.download_data, name ='download-data'),
]
