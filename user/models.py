from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.
number = RegexValidator(r'^([\s\d]+)$', 'Only numbers are allowed.')
GENDER_CHOICES = (('M', _('Male')), ('F', _('Female')))

class Department(models.Model):
	""" Department model """
	name = models.CharField(max_length=1024, verbose_name="DEPARTMENT")

class JobRole(models.Model):
	""" JobRole model """
	title = models.CharField(max_length=1024, verbose_name="TITLE")

class Employee(models.Model):
    """ Employee model """
    user_id = models.IntegerField(verbose_name='USER ID', unique=True)
    
    firstname = models.CharField(verbose_name='FIRST NAME', max_length=50)
    middlename = models.CharField(verbose_name='MIDDLE NAME', max_length=50)
    lastname = models.CharField(verbose_name='LAST NAME', max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    birthday = models.DateField(verbose_name='BIRTHDAY')
    
    province = models.CharField(verbose_name='PROVINCE', max_length=50)
    city = models.CharField(verbose_name='CITY', max_length=50)
    street = models.CharField(verbose_name='STREET', max_length=50)
    
    zip = models.CharField(verbose_name='ZIP', max_length=4, validators=[number])
    contact = models.CharField(verbose_name='CONTACT', max_length=11, validators=[number])

    hireday = models.DateField(verbose_name='HIREDAY')
    job_role = models.ForeignKey(JobRole, on_delete=models.PROTECT, blank=True, null=True, verbose_name='JOB ROLE')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True, verbose_name='DEPARTMENT')

    start_date = models.DateField(blank=True, null=True, verbose_name='START DATE')
    end_date = models.DateField(null=True, blank=True, verbose_name='END DATE')

    def __unicode__(self):
        return "%s"%self.user