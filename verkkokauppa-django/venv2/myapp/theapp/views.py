from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json

def main(request):
    
    return render(request, 'index.html')

def products(request):

    with open('products.json', 'r') as file:
        data = json.load(file)    

    return render(request, 'products.html',  {"json_data": data})

def cart(request):

    return render(request, 'cart.html')
