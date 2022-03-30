from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm
from django.contrib import messages
from django.urls import reverse
from .models import Employee
# Create your views here.
def index(request):
    return render(request, 'user/index.html',{})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'user/employee-list.html', {'employees': employees, 'page_title': 'Employee List'})

def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly registered!')
            return HttpResponseRedirect(reverse('register-employee'))
        else:
            messages.error(request, 'Registration failed!')
    else:
        form = EmployeeForm()
    return render(request, 'user/register-employee.html',{'form': form, 'page_title': 'Register User'})