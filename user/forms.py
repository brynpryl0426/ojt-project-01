from django import forms
from .models import Employee
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

number = RegexValidator(r'^([\s\d]+)$', 'Only numbers are allowed.')

GENDER_CHOICES = (('M', _('Male')), ('F', _('Female')))

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('user_id',)

    firstname = forms.CharField(label='FIRST NAME')
    lastname = forms.CharField(label='LAST NAME')
    gender = forms.ChoiceField()
    birthday = forms.DateField(label='BIRTHDAY')
    fullname = forms.CharField(label="Fullname")
    province = forms.CharField(label='PROVINCE')
    city = forms.CharField(label='CITY')
    barangay = forms.CharField(label='BARANGAY')
    contact = forms.CharField(label='CONTACT')
    hireday = forms.DateField(label='HIREDAY')

class MachineForm(forms.Form):
    ip = forms.GenericIPAddressField(label='IP Address', required=True)
    port = forms.CharField(label='Port', max_length=5, required=True, validators=[number])