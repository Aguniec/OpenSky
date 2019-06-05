from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Handle the  homepage


def home(request):
    return HttpResponse("<h1> Page home </h1>")


def about(request):
    return HttpResponse("<h1> Blog about</h1>")


# Create your views here.
