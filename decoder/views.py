from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'decoder/base.html', {})


def lnurl(request):

    return render(request, 'decoder/lnurl.html', {})

def lninvoice(request):

    return render(request, 'decoder/lninvoice.html', {})
def lnaddress(request):

    return render(request, 'decoder/lnadress.html', {})
    