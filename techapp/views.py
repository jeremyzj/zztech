from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render
from .models import ClientMessage

def index(request):
    context = {}
    return render(request, "techapp/index.html", context)


def message(request):
    print(request.POST["message"], request.POST["name"], request.POST["email"])
    message = ClientMessage(message=request.POST["message"], name=request.POST["name"], email=request.POST["email"])
    message.save()
    return render(request, "techapp/result.html", {})