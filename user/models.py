from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.
number = RegexValidator(r'^([\s\d]+)$', 'Only numbers are allowed.')
GENDER_CHOICES = (('M', _('Male')), ('F', _('Female')))

SUFFIX_CHOICES = (
    ("SR.", "SENIOR"),
    ("JR.", "JUNIOR"),
    ("I", "I"),
    ("II", "II"),
    ("III", "III"),
    ("IV", "IV"),
    ("V", "V"),
    ("VI", "VI"),
    ("VII", "VII"),
    ("VIII", "VIII"),
)

class Department(models.Model):
    """ Department model """

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        db_table = 'tbl_department'

    name = models.CharField(max_length=1024, verbose_name="DEPARTMENT")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Department, self).save(*args, **kwargs)

class JobRole(models.Model):
    """ JobRole model """
    
    class Meta:
        verbose_name = 'Job Role'
        verbose_name_plural = 'Job Roles'
        db_table = 'tbl_job_role'

    title = models.CharField(max_length=1024, verbose_name="TITLE")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super(JobRole, self).save(*args, **kwargs)

class Employee(models.Model):
    """ Employee model """

    class Meta:
            verbose_name = 'Employee'
            verbose_name_plural = 'Employees'
            db_table = 'tbl_employee'
    user_id = models.IntegerField(verbose_name="USER ID", unique=True)
    firstname = models.CharField(verbose_name='FIRST NAME', max_length=50, blank=True, null=True)
    middle_initial = models.CharField(verbose_name='MIDDLE INITIAL', max_length=1, blank=True, null=True)
    lastname = models.CharField(verbose_name='LAST NAME', max_length=50, blank=True, null=True)
    name_suffix = models.CharField(max_length=10, null=True, blank=True, choices=SUFFIX_CHOICES, verbose_name="Suffix")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birthday = models.DateField(verbose_name='BIRTHDAY', blank=True, null=True)

    fullname = models.CharField(max_length=255,verbose_name="Fullname", blank=True, null=True)
    
    province = models.CharField(verbose_name='PROVINCE', max_length=50, blank=True, null=True)
    city = models.CharField(verbose_name='CITY', max_length=50, blank=True, null=True)
    barangay = models.CharField(verbose_name='BARANGAY', max_length=50, blank=True, null=True)
    street = models.CharField(verbose_name='STREET', max_length=50, blank=True, null=True)
    
    zip = models.CharField(verbose_name='ZIP', max_length=4, validators=[number], blank=True, null=True)
    contact = models.CharField(verbose_name='CONTACT', max_length=11, validators=[number], blank=True, null=True)

    hireday = models.DateField(verbose_name='HIREDAY', blank=True, null=True)
    job_role = models.ForeignKey(JobRole, on_delete=models.PROTECT, blank=True, null=True, verbose_name='JOB ROLE')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True, verbose_name='DEPARTMENT')

    start_date = models.DateField(blank=True, null=True, verbose_name='START DATE')
    end_date = models.DateField(null=True, blank=True, verbose_name='END DATE')

    def __str__(self):
        return str(self.user_id)

    def getfullname(self):
        if self.middle_initial is None and self.name_suffix is None:
            self.fullname = '{}, {}'.format(self.lastname, self.firstname)
        elif self.middle_initial is None:
            self.fullname = '{}, {}, {}'.format(self.lastname, self.name_suffix, self.firstname)
        elif self.name_suffix is None:
            self.fullname = '{}, {} {}.'.format(self.lastname, self.firstname, self.middle_initial)
        else:   
            self.fullname = '{}, {}, {} {}.'.format(self.lastname, self.name_suffix, self.firstname, self.middle_initial)
        return self.fullname

    def save(self, *args, **kwargs):
        if self.firstname is not None:
            self.firstname = self.firstname.upper()
        if self.middle_initial is not None:
            self.middle_initial = self.middle_initial.upper()
        if self.lastname is not None:
            self.lastname = self.lastname.upper()

        self.fullname = self.getfullname()
        
        if self.city is not None:
            self.city = self.city.upper()
        if self.barangay is not None:
            self.barangay = self.barangay.upper()
        if self.street is not None:
            self.street = self.street.upper()
            
        super(Employee, self).save(*args, **kwargs)

class Machines(models.Model):
    """ Machine model """
    ip = models.GenericIPAddressField(verbose_name='IP ADDRESS')
    port = models.CharField(verbose_name='PORT', max_length=5, validators=[number])
    machine_name = models.CharField(verbose_name='MACHINE NAME', max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ip
    
    def save(self, *args, **kwargs):
        self.machine_name = self.ip
        super(Machines, self).save(*args, **kwargs)