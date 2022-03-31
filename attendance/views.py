from django.shortcuts import render
from zk import ZK, const
from django.contrib import messages

from user.models import Employee
from .models import EmployeeCheckInOut

# Create your views here.
def employee_logs(request):
    conn = None
    ip = None
    port = None
    ip = None

  
    zk = ZK('192.168.10.201', port=4370, timeout=60, password=0, force_udp=False, ommit_ping=False)
    try:
        # connect to device
        conn = zk.connect()
        # disable device, this method ensures no activity on the device while the process is run
        conn.disable_device()
        # another commands will be here!
        # Get All Users
        attendances = conn.get_attendance()
        
        for attendance in attendances:
            print(attendance.user_id)
            print(attendance.timestamp)
            if not EmployeeCheckInOut.objects.filter(employee=Employee.objects.get(user_id=attendance.user_id), checktime=attendance.timestamp).exists():
                EmployeeCheckInOut.objects.create(employee=Employee.objects.get(user_id=attendance.user_id), checktime=attendance.timestamp)

        # Test Voice: Say Thank You
        conn.test_voice()
        # re-enable device after all commands already executed
        conn.enable_device()
        messages.success(request, 'Employees Successfuly registered!')
    except Exception as e:
        print ("Process terminate : {}".format(e))
        print(type(e).__name__, e.args)
        messages.error(request, "Process terminate : {}".format(e))
    finally:
        if conn:
            conn.disconnect()
      
    return render(request, 'attendance/employee-logs.html', {'attendances': attendances, 'page_title': 'Employee Logs'})