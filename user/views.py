from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'user/index.html',{})

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly registered!')
            return HttpResponseRedirect(reverse('register-employee'))
        else:
            messages.error(request, 'Registration failed!')
    else:
        form = EmployeeForm()
    return render(request, 'user/register-employee.html',{'form': form, 'page_title': 'Register User'})