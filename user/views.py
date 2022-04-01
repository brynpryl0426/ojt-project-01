from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmployeeForm, MachineForm
from django.contrib import messages
from django.urls import reverse
from .models import Employee
from zk import ZK, const

# Create your views here.
def index(request):
    return render(request, 'user/index.html',{})

def employee_list(request):
    employees = Employee.objects.all().order_by('-date_updated')
    return render(request, 'user/employee-list.html', {'employees': employees, 'page_title': 'Employee List'})

def download_data(request):
    
    conn = None
    ip = None
    port = None
    ip = None

    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            zk = ZK(request.POST.get('ip'), port=int(request.POST.get('port')), timeout=60, password=0, force_udp=False, ommit_ping=False)
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
                    
                    if not Employee.objects.filter(user_id=user.user_id).exists():
                        Employee.objects.create(user_id=user.user_id, firstname=user.name, lastname=user.name)

                # Test Voice: Say Thank You
                conn.test_voice()
                # re-enable device after all commands already executed
                conn.enable_device()
                messages.success(request, 'Employees Successfuly registered!')
                return HttpResponseRedirect(reverse('employee-list'))
            except Exception as e:
                print ("Process terminate : {}".format(e))
                print(type(e).__name__, e.args)
                messages.error(request, "Process terminate : {}".format(e))
            finally:
                if conn:
                    conn.disconnect()
            ip = request.POST.get('ip')
    else:
        form = MachineForm(initial={'ip':ip,'port': 4370})
    return render(request, 'user/download-data.html',{'page_title': 'Download Data', 'form': form})


def update_employee(request, user_id):
    try:
        employee = Employee.objects.get(user_id=user_id)
        form = EmployeeForm(request.POST or None, instance=employee)
        if request.method == 'POST':
            
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfuly updated!')
                return HttpResponseRedirect(reverse('employee-list'))
            else:
                messages.error(request, 'Update failed!')
    except Employee.DoesNotExist:
        messages.error(request, 'Employee does not exist!')
        return HttpResponseRedirect(reverse('employee-list'))
    return render(request, 'user/update-employee.html',{'form': form, 'page_title': 'Register User'})