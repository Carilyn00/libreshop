from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'shop/home.html')

def product_page(request):
    return render(request, 'shop/product.html')
