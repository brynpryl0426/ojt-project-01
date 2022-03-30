from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm
from django.contrib import messages
from django.urls import reverse
from .models import Employee
from zk import ZK, const

# Create your views here.
def index(request):
    return render(request, 'user/index.html',{})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'user/employee-list.html', {'employees': employees, 'page_title': 'Employee List'})

def download_data(request):
    
    conn = None
    ip = None
    port = None

    if request.method == 'POST':
        ip = request.POST.get('ip')
        port = request.POST.get('port')
    zk = ZK('192.168.10.7', port=4370, timeout=60, password=0, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Get All Users
        users = conn.get_users()
        for user in users:
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'
            Employee.objects.create(user_id=user.user_id)

        # Test Voice: Say Thank You
        conn.test_voice()
        # re-enable device after all commands already executed
        conn.enable_device()
    except Exception as e:
        print ("Process terminate : {}".format(e))
        print(type(e).__name__, e.args)
        messages.error(request, "Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()
    return render(request, 'user/download-data.html',{'page_title': 'Download Data'})


def update_employee(request, user_id):
    employee = Employee.objects.get(user_id=user_id)
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