from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderCreateForm

@login_required
def order_create(request):
    """Vue pour créer une nouvelle commande depuis le panier"""
    cart = Cart(request)
    
    # Vérifier que le panier n'est pas vide
    if len(cart) == 0:
        messages.warning(request, "Votre panier est vide.")
        return redirect('products:list')
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Créer la commande
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()
            
            # Créer les items de la commande
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            # Vider le panier
            cart.clear()
            
            messages.success(request, f"Commande #{order.id} créée avec succès !")
            return redirect('orders:detail', order_id=order.id)
    else:
        form = OrderCreateForm()
    
    return render(request, 'orders/create.html', {
        'cart': cart,
        'form': form
    })


@login_required
def order_list(request):
    """Vue pour afficher la liste des commandes de l'utilisateur"""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Vue pour afficher les détails d'une commande"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})


@login_required
def order_cancel(request, order_id):
    """Vue pour annuler une commande"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # On peut annuler seulement si la commande est en attente
    if order.status == 'pending':
        order.status = 'cancelled'
        order.save()
        messages.success(request, f"Commande #{order.id} annulée.")
    else:
        messages.error(request, "Cette commande ne peut pas être annulée.")
    
    return redirect('orders:detail', order_id=order.id)