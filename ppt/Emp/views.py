from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import emp,Testimonial
from .forms import Feedbackform,Empform
# Create your views here.
def emp_home(request):

    emps=emp.objects.all()



    return render(request,"emp/home.html",{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e= emp()
        e.name=emp_name
        e.emp_mail=emp_id
        e.phone_number=emp_phone
        e.department=emp_department
        e.status=emp_working
        e.address=emp_address
        if emp_working is None:
            e.status=False
        else:
            e.status=True

        e.save()    



        return redirect("/emp/home")
    form=Empform()
    return render(request,"emp/add_emp.html",{'form':form})

def delete_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    Emp.delete()
    return redirect("/emp/home/")
def update_emp(request,emp_id):
    Emp=emp.objects.get(pk=emp_id)
    
    return render(request,"emp/update_emp.html/",{'emp':Emp})

def do_update_emp(request,emp_id):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        Emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_mail=Emp_id
        e.phone_number=emp_phone
        e.department=emp_department
        e.status=emp_working
        e.address=emp_address
        if emp_working is None:
            e.status=False
        else:
            e.status=True

        e.save()    




    return redirect("/emp/home/")

def testimonials(request):

    test=Testimonial.objects.all()
    return render(request,"emp/testimonials.html",{'test':test})

def feedback(request):
    if request.method=="POST":
        form=Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            print("data saved") 
            print(form.cleaned_data['name'])
            
            return super().form_valid(form)
        
    else:
        form=Feedbackform
    return render(request,'emp/feedback.html',{'form':form})