from django import forms
from .models import Employee
from django.core.validators import RegexValidator

number = RegexValidator(r'^([\s\d]+)$', 'Only numbers are allowed.')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('user_id',)

class MachineForm(forms.Form):
    ip = forms.GenericIPAddressField(label='IP Address', required=True)
    port = forms.CharField(label='Port', max_length=5, required=True, validators=[number])