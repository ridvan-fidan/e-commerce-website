from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def product(request):
    ürünler = Product.objects.all()
    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')
        ürünler = Product.objects.filter(isim__icontains = search)

    context = {
       'ürünler':ürünler 
    }
    return render(request, 'shop.html',context)

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')