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
    response_dict = ''
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

        response_dict = {}

        for i in range(len(parsedData)):
           response_dict = parsedData[i]

    return render(request, 'decoder/lnurl.html', {'response':response_dict})


def lninvoice(request):
    response_dict = ''
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
            userData['Destination'] = data['data']['destination']
            userData['created_at'] = data['data']['created_at']
            userData['expires_at'] = data['data']['expires_at']
            userData['id'] = data['data']['id']
            userData['is_expired'] = data['data']['is_expired']
            userData['safe_tokens'] = data['data']['safe_tokens']
            userData['tokens'] = data['data']['tokens']

            
        parsedData.append(userData)

        response_dict = {}

        for i in range(len(parsedData)):
           response_dict = parsedData[i]


    return render(request, 'decoder/lninvoice.html', {'response':response_dict})


def lnaddress(request):
    response_dict = ''
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
            userData['tag'] = data['data']['tag']
            userData['callback'] = data['data']['callback']
            userData['description'] = data['data']['description']
            userData['satMinSendable'] = data['data']['satMinSendable']
            userData['satMaxSendable'] = data['data']['satMaxSendable']
            
        parsedData.append(userData)

        response_dict = {}

        for i in range(len(parsedData)):
           response_dict = parsedData[i]

    return render(request, 'decoder/lnaddress.html', {'response':response_dict})
    