from django.shortcuts import render,redirect
from .models import Product
# Create your views here.
def index(request):

    products = Product.objects.all()
    return render(request,"Products/list.html",{'products':products})

def newProductForm(request,pk):
    if request.method == 'POST':
        name = request.POST['name']
        weight = request.POST['weight']
        price = request.POST['price']

        p = Product.objects.create(name=name,weight=weight,price=price)
        p.save()
        return redirect('index')

    return render(request,"Products/newproduct.html")