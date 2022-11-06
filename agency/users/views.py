from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def CustomForm(request):
    userform = UserForm()
    return render(request, "index.html", {"form": userform})