from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_student(request):
    d={'ESFO':StudentMF()}

    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Student is created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_student.html',d)