from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.http import HttpResponse

def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('Data not insertted...!')
    return render(request,'Student.html',d)