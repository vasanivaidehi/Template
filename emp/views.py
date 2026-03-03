from django.shortcuts import render,redirect
from .models import Emp
from .forms import EmpForm

# Create your views here.

def emp_add(request):
    form=EmpForm()

    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    return render (request,'emp/form.html',{'form':form})

def emp_list(request):
    data=Emp.objects.all()
    return render(request,'emp/list.html',{'data':data})

def emp_edit(request,id):
    emp=Emp.objects.get(id=id)
    form=EmpForm(instance=emp)

    if request.method=='POST':
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    return render(request,'emp/form.html',{'form':form})

def emp_delete(request,id):
    emp=Emp.objects.get(id=id)
    emp.delete()
    return redirect('emp_list')

def emp_bulk_delete(request):
    if request.method=="POST":
        ids=request.POST.getlist('selected_ids')#multiple checkbox values
        Emp.objects.filter(id__in=ids).delete()#badha selected records
    return redirect('emp_list')

