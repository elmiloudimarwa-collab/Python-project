from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderForm

@login_required
def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = 0
            order.save()
            return redirect("order_success")
    else:
        form = OrderForm()

    return render(request, "orders/checkout.html", {"form": form})

@login_required
def order_success(request):
    return render(request, "orders/success.html")
