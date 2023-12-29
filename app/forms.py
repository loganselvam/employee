from django import forms
from app.models import Employee

class employeeForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    position = forms.CharField(widget=forms.TextInput)
    salary = forms.IntegerField(widget=forms.NumberInput)
    hire_date = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }))
    department = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)

class updateform(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    position = forms.CharField(widget=forms.TextInput)
    salary = forms.IntegerField(widget=forms.NumberInput)
    hire_date = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }))
    department = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)

    def __init__(self,uid,*args,**kwargs):
        super().__init__(*args,**kwargs)
        data = Employee.objects.get(id=uid)
        self.fields['first_name'].initial =data.first_name
        self.fields['last_name'].initial =data.last_name
        self.fields['position'].initial =data.position
        self.fields['salary'].initial =data.salary
        self.fields['hire_date'].initial =data.hire_date
        self.fields['department'].initial =data.department
        self.fields['email'].initial =data.email

