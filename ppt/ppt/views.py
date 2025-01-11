from django.http import HttpResponse
from django.shortcuts import render
import datetime
def Home(request):
    isActive=False
    if request.method=="POST":
        check=request.POST.get('check')
        print(check)
        if check is not None:
         isActive=False
        else:
            isActive=True

    date=datetime.datetime.now()
   
    name="PUSHPENDRA TIWARI"
    list_of_programs= [

      'firstly practice DSA',

      'secondly add something to project',

      'continue your course']
    
    student={
      'student_name':"Sam",
      'College':"GIC",
      'City':"Mahoba"

     }
    data={
        'date':date,
     'isActive':isActive,
     'name':name,
     'date':date,
     'list_of_programs':list_of_programs,
     'student_data':student
     }
    


    return render(request,"Home.html",data)

def about(request):
    
    return render(request,"about.html",{})


def services(request):
    return render(request,"services.html")