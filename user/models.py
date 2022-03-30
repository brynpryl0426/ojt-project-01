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
    
    firstname = models.CharField(verbose_name='FIRST NAME', max_length=50)
    middle_initial = models.CharField(verbose_name='MIDDLE INITIAL', max_length=1, blank=True, null=True)
    lastname = models.CharField(verbose_name='LAST NAME', max_length=50)
    name_suffix = models.CharField(max_length=10, null=True, blank=True, choices=SUFFIX_CHOICES, verbose_name="Suffix")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name='BIRTHDAY')

    fullname = models.CharField(max_length=255,verbose_name="Fullname")
    
    province = models.CharField(verbose_name='PROVINCE', max_length=50)
    city = models.CharField(verbose_name='CITY', max_length=50)
    barangay = models.CharField(verbose_name='BARANGAY', max_length=50)
    street = models.CharField(verbose_name='STREET', max_length=50, blank=True, null=True)
    
    zip = models.CharField(verbose_name='ZIP', max_length=4, validators=[number], blank=True, null=True)
    contact = models.CharField(verbose_name='CONTACT', max_length=11, validators=[number])

    hireday = models.DateField(verbose_name='HIREDAY')
    job_role = models.ForeignKey(JobRole, on_delete=models.PROTECT, blank=True, null=True, verbose_name='JOB ROLE')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True, verbose_name='DEPARTMENT')

    start_date = models.DateField(blank=True, null=True, verbose_name='START DATE')
    end_date = models.DateField(null=True, blank=True, verbose_name='END DATE')

    def __unicode__(self):
        return "%s"%self.user

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
        self.firstname = self.firstname.upper()
        if self.middle_initial is not None:
            self.middle_initial = self.middle_initial.upper()
        self.lastname = self.lastname.upper()
        self.fullname = self.getfullname()
        self.city = self.city.upper()
        self.barangay = self.barangay.upper()
        if self.street is not None:
            self.street = self.street.upper()
            
        super(Employee, self).save(*args, **kwargs)