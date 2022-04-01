from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from zk import ZK, const
from django.contrib import messages
from user.forms import MachineForm
import collections
from user.models import Employee
from .models import EmployeeCheckInOut
import pandas as pd
import numpy as np
from datetime import datetime


# Create your views here.
def employee_logs(request):
    conn = None
    ip = None
    port = None
    attendances = None

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

                newtime = datetime.today()
                conn.set_time(newtime)

                attendances = conn.get_attendance()
                employees = Employee.objects.all()
                
                emp_user_id = []
                emp_names = []

                for emp in employees:
                    emp_user_id.append(emp.user_id)
                    emp_names.append(emp.fullname)

                df1 = pd.DataFrame({
                    'user_id': emp_user_id,
                    'emp_names': emp_names
                })

                att_user_id = []
                timestamps = []

                for attendance in attendances:
                    att_user_id.append(attendance.user_id) 
                    timestamps.append(attendance.timestamp)

                df2 = pd.DataFrame({
                    'user_id': att_user_id,
                    'timestamps': timestamps
                }).sort_values('timestamps',ascending=False)

                df1['user_id']=df1['user_id'].astype(int)
                df2['user_id']=df2['user_id'].astype(int)

                print(df1)
                print(pd.merge(df2,df1))
                checkinout_df = pd.merge(df2,df1)
                # Test Voice: Say Thank You
                conn.test_voice()
                # re-enable device after all commands already executed
                conn.enable_device()
                messages.success(request, 'Employees Successfuly registered!')
                return render(request, 'attendance/employee-logs.html', {'attendances': checkinout_df, 'page_title': 'Employee Logs', 'form': form})
            except Exception as e:
                print ("Process terminate : {}".format(e))
                print(type(e).__name__, e.args)
                messages.error(request, "Process terminate : {}".format(e))
            finally:
                if conn:
                    conn.disconnect()
    else:
        form = MachineForm(initial={'ip':ip,'port': 4370})
      
    return render(request, 'attendance/employee-logs.html', {'attendances': attendances, 'page_title': 'Employee Logs', 'form': form})

def upload_employee_logs(request):
    pass
    # for attendance in attendances:
                    # print(attendance.user_id)
                    # print(attendance.timestamp)
                    # if not EmployeeCheckInOut.objects.filter(employee=Employee.objects.get(user_id=attendance.user_id), checktime=attendance.timestamp).exists():
                    #     EmployeeCheckInOut.objects.create(employee=Employee.objects.get(user_id=attendance.user_id), checktime=attendance.timestamp)
    