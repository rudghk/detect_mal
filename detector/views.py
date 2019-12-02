from django.shortcuts import render
from .models import Black

import json
import urllib.request

# Create your views here.

def home(request):
    return render(request, 'index.html')

#@api_view(['GET'])
def black_list(request):
    apikey = '853a551ae6d19cfa01e82e1f9a5f8dc31709e14ab173bcff5c62c35d53bce734'
    url = "http://data.phishtank.com/data/"+apikey+"/online-valid.json"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        result = json.loads(response_body)
        for element in result:
            phish_id = element['phish_id']
            url = element['url']
            black = Black()
            black.black_id = phish_id
            black.url = url
            black.save()

