from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    data = request.META['QUERY_STRING'].split('=')[1]
    return HttpResponse(data)


def exchange(request, value):
    return HttpResponse(value)
