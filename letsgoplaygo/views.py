from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request, "base.html")

def get_users(request):

    data = {"users": User.objects.all()}
    return render(request, "users.html", context=data)

def create_user(request):

    if request.method == "POST":
        user_form =  UserForm(data=request.POST)
        if user_form.is_valid():
            username = request.POST.get("username", None)
            password = request.POST.get("password1", None)
            user = User.objects.create_user(username, password=password)
            user.save()
            return redirect("/")
        return render(request, "authpage.html", {"form": user_form})

    return render(request, "authpage.html", {"form":UserForm})