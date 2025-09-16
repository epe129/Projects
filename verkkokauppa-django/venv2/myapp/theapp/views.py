from django.http import HttpResponse
from django.template import loader
# Create your views here.

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def products(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render())

def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())
