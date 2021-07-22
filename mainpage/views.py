from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from .scraper import *
from .scraperflip import *
flipkart="https://www.flipkart.com/"
amazon="https://www.amazon.in/"
# Create your views here.
def index(request):
     if request.method == 'POST':
         form = NameForm(request.POST)
         if form.is_valid():
             URL=form.cleaned_data["URL2"]
             
             budget=form.cleaned_data["budget2"]
             toemail=form.cleaned_data["email2"]
             if flipkart in URL:
                converted_price=check_price_flip(URL=URL,budget=budget,toemail=toemail)
             elif amazon in URL:
                converted_price=check_price(URL=URL,budget=budget,toemail=toemail)
             return render(request,'mainpage/index.html',{'form': form,'URL':URL,'budget':converted_price})
     return render(request,'mainpage/index.html')
# Create your views here.
