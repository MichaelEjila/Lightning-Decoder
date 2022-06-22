from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Base Page")


def lnurl(request):
    return HttpResponse("Lightning Url page")

def lninvoice(request):
    return HttpResponse("Lightning Invoice page")

def lnaddress(request):
    return HttpResponse("Lightning Address page")
    