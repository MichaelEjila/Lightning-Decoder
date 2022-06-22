from django.http import HttpResponse
from django.shortcuts import render
from decouple import config
import json
import requests

# Create your views here.
def index(request):
    return HttpResponse("Base Page")

#Extract data in its raw form
'''
def lnurl(request):
    url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnurl"
    payload = {"encodedLnUrl": "lnurl1dp68gurn8ghj7cnfw3ex2enfd3kzumt99amrztmvde6hymzlwpshjtekxycnvef48yun2wp4xs6kgvpsx93kgdp5ve3nvk9dgjd"}
    headers = {
        "Accept": "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + api_key
    }
    response = requests.post(url, json=payload, headers=headers)
    content = response.text
    return HttpResponse(content) 
'''

#Extract data in an organized form
def lnurl(request):
    api_key = config('key')
    url = "https://sandboxapi.bitnob.co/api/v1/lnurl/decodelnurl"
    payload = {"encodedLnUrl": "lnurl1dp68gurn8ghj7cnfw3ex2enfd3kzumt99amrztmvde6hymzlwpshjtekxycnvef48yun2wp4xs6kgvpsx93kgdp5ve3nvk9dgjd"}
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
    return HttpResponse(parsedData)


def lninvoice(request):
    return HttpResponse("Lightning Invoice page")


def lnaddress(request):
    return HttpResponse("Lightning Address page")
    