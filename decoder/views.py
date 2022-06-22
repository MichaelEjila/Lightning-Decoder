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
    if request.method == 'POST':
        address = request.POST.get('lnaddress')
    API_KEY = config('KEY')
    url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnaddress"

    payload = {"lnAddress": "mikeoxygen@bitnob.io"}
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer "+ API_KEY
}
    jsonList = []
    response = requests.post(url, json=payload, headers=headers)
    content = response.text
    jsonList.append(json.loads(response.content))
    parsedData = []
    userData = {}
    for data in jsonList:
     userData['status'] = data['status']
     userData['message'] = data['message']
     userData['data-tag'] = data['data']['tag']
     userData['data-metadata'] = data['data']['metadata']
     

    parsedData.append(userData)
    return render(request, 'decoder/lnaddress.html', {'response':parsedData})


    