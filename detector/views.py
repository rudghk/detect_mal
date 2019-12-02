from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import White

# Create your views here.
def home(request):
    return render(request, 'index.html')

def get_WhiteList(request):
    catagory=['Adult', 'Arts', 'Business', 'Computers','Games','Reference','Regional','Science','Shopping','Society','Health','Home','Kids_and_Teens','News','Recreation','Sports','World' ]
    for i in white_list_url:
        req=requests.get('https://www.alexa.com/topsites/category/Top/'+catagory[i])
        html=req.text
        soup=BeautifulSoup(html, "html.parser")
        pkg_list=soup.findAll("div","td DescriptionCell")

        for i in pkg_list: 
        title=i.findAll('a')
        whiteUrl=str(title)[str(title).find('siteinfo/')+9:str(title).find('">')]
        insert_white(whiteUrl)

def insert_white(whiteUrl):
    white=White()
    white.url=whiteUrl
    white.save()
