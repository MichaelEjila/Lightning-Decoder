from django.http import HttpResponse
from django.shortcuts import render
import requests
from decouple import config
import json

# Create your views here.
def index(request):
    
    return render(request, 'decoder/base.html', {})


def lnurl(request):

    return render(request, 'decoder/lnurl.html', {})

def lninvoice(request):
    parsedData = []
    if request.method == 'POST':
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
            userData['is_expired'] = data['is_expired']
            
        parsedData.append(userData)


    return render(request, 'decoder/lninvoice.html', {'response':parsedData})

def lnaddress(request):

    return render(request, 'decoder/lnaddress.html', {})
    