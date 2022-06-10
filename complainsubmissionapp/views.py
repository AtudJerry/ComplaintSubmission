from email.errors import FirstHeaderLineIsContinuationDefect
from django.http import HttpResponse
from django.shortcuts import render

from complainsubmissionapp.forms import Studentform
from .models import Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Your complain has been submitted to the lecturer successfully</h1>")
    else:
        form = Studentform()
    context = {
        'form' : form,
        }


    return render(request,'index.html',context)