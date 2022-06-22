from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from decouple import config

# Create your views here.
def index(request):
    return render(request, 'decoder/base.html', {})


def lnurl(request):

    return render(request, 'decoder/lnurl.html', {})

def lninvoice(request):

    return render(request, 'decoder/lninvoice.html', {})
    
def lnaddress(request):
    parsedData = []
    response = []
    
    if request.method == 'POST':
        address = request.POST.get('lnaddress')
        print(address)
        API_KEY = config('KEY')
        url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnaddress"

        payload = {"request": address}
        headers = {
           "Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": "Bearer "+ API_KEY
        }
        jsonList = []
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        content = response.text
        jsonList.append(json.loads(response.content))
        userData = {}
       
        parsedData.append(userData)
    return render(request, 'decoder/lnaddress.html', {'response':response})


    