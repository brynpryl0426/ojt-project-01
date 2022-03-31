from django.db import models
from user.models import Employee

# Create your models here.
class EmployeeCheckInOut(models.Model):

    class Meta:
        verbose_name = 'Employee Check In/Out'
        verbose_name_plural = 'Employee Check In/Out'
        db_table = 'tbl_employee_check_in_out'
        
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='Employee')
    checktime = models.DateTimeField(verbose_name='Check Time')

    def __str__(self):
        return f"{str(self.employee)} - {str(self.checktime)}"