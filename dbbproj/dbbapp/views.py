from django.shortcuts import render,redirect
from .models import Userdb
from .forms import UserForm
from django.contrib import messages
# Create your views here.

def UserView(request):
    frm={}
    if request.method=="POST":
        frm = UserForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request,"saves the record")
            return redirect("dispall")
    else:
        frm = Userdb()
    return render(request,"index.html",{'form':frm})

def showstud(request):
    students = Userdb.objects.all()
    context = {'students':students}
    return render(request,"showstud.html",context)
