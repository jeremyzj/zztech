from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "techapp/index.html", context)


def message(request):
    print(request.POST["message"], request.POST["name"], request.POST["email"])
    context = {}
    return render(request, "techapp/index.html", context)