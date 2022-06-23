from django.http import HttpResponse
from django.shortcuts import render

import requests
from decouple import config
import json

# Create your views here.
def index(request):
    
    return render(request, 'decoder/base.html', {})
  
#Extract data in an organized form
def lnurl(request):
    parsedData = ''
    if request.method == 'POST':
        lightning_url = request.POST.get('lnurl')

        api_key = config('key')
        url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnurl"
        payload = {"encodedLnUrl": lightning_url}
        headers = {
            "Accept": "application/json",
            "Content-Type" : "application/json",
            "Authorization" : "Bearer " + api_key
        }
        response = requests.post(url, json=payload, headers=headers)

        jsonList = []
        jsonList.append(json.loads(response.content))
        parsedData = []
        lnData = {}
        for data in jsonList:
            lnData['status'] = data['status']
            lnData['message'] = data['message']
            lnData['tag'] = data['data']['tag']
            lnData['callback'] = data['data']['callback']
            lnData['description'] = data['data']['description']
            lnData['satMinSendable'] = data['data']['satMinSendable']
            lnData['satMaxSendable'] = data['data']['satMaxSendable']
        parsedData.append(lnData)

    return render(request, 'decoder/lnurl.html', {'response':parsedData})


def lninvoice(request):
    parsedData = ''
    if request.method == 'POST':
        parsedData = []
        invoice = request.POST.get('lninvoice')
        
        api_key = config('key')
        url = "https://sandboxapi.bitnob.co/api/v1/wallets/ln/decodepaymentrequest"
    
        payload = {"request": invoice}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        
        response = requests.post(url, json=payload, headers=headers)
        jsonList = []
        jsonList.append(json.loads(response.content))
        userData = {}
        for data in jsonList:
            userData['status'] = data['status']
            userData['message'] = data['message']
            userData['chain address'] = data['data']['chain_address']
            userData['Description'] = data['data']['description']
            userData['expires_at'] = data['data']['expires_at']
            
        parsedData.append(userData)


    return render(request, 'decoder/lninvoice.html', {'response':parsedData})


def lnaddress(request):
    parsedData = ''
    if request.method == 'POST':
        parsedData = []
        ln = request.POST.get('lnaddress')

        api_key = config('key')
        url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnaddress"

        payload = {"lnAddress": ln}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }

        response = requests.post(url, json=payload, headers=headers)
        jsonList = []
        jsonList.append(json.loads(response.content))
        userData = {}
        for data in jsonList:
            userData['status'] = data['status']
            userData['message'] = data['message']
            userData['data'] = data['data']
            
        parsedData.append(userData)

    return render(request, 'decoder/lnaddress.html', {'response':parsedData})
    