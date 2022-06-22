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
    API_KEY = config('KEY')
    url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnaddress"

    payload = {"lnAddress": "mikeoxygen@bitnob.io"}
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer "+ API_KEY
}
    jsonList = []
    req = requests.post(url, json=payload, headers=headers)
    content = req.text
    jsonList.append(json.loads(req.content))
    parsedData = []
    userData = {}
    for data in jsonList:
     userData['status'] = data['status']
     userData['message'] = data['message']
     userData['data-tag'] = data['data']['tag']
     userData['data-metadata'] = data['data']['metadata']
     



    parsedData.append(userData)
    return HttpResponse(parsedData)
    print(req.text)

    