from django.shortcuts import render

def cart_detail(request):
    # Pour l'instant, juste une page de test
    return render(request, "cart/detail.html")
