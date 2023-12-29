from django.shortcuts import render
from app.forms import employeeForm,updateform
from app.models import Employee
from django.http import HttpResponse
# Create your views here.
def employeeView(request):
    form = employeeForm().as_p
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            position =  form.cleaned_data['position']
            sal = form.cleaned_data['salary']
            h_date = form.cleaned_data['hire_date']
            dept = form.cleaned_data['department']
            email = form.cleaned_data['email']
            # inserting the data in the table
            Employee.objects.create(first_name=f_name,last_name=l_name,position=position,salary=sal,hire_date=h_date,department=dept,email=email)
            return render(request,'insmsg.html')

    return render(request,'empdetail.html',{'form':form})

def viewemp(request,vid):
    data=Employee.objects.get(id=vid)
    print(data)
    return render(request,'empView.html',{'data':data})

def empupdate(request,uid):
    form = updateform(uid)
    if request.method=='POST':
        form =updateform(uid,request.POST)
        if form.is_valid():
            data = Employee.objects.get(id=uid)
            data.first_name = form.cleaned_data['first_name']
            data.last_name  = form.cleaned_data['last_name']
            data.position = form.cleaned_data['position']
            data.salary = form.cleaned_data['salary']
            data.hire_date = form.cleaned_data['hire_date']
            data.department = form.cleaned_data['department']
            data.email = form.cleaned_data['email']
            data.save()
            return render(request,'updatemessage.html')
    return render(request,'updateemp.html',{'form':form})

def empdelete(request,did):
    data = Employee.objects.get(id=did)
    data.delete()
    return render(request,'delmessage.html')


def empdetails(request):
    data = Employee.objects.all()
    return render(request,'viewemp.html',{'data':data})

