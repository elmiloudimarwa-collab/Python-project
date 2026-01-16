from django.shortcuts import render, redirect
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)

    # TEMPORARY price for now
    cart.add(product_id=product_id, price=10)

    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart_detail')
