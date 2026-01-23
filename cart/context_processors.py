def cart_counter(request):
    cart = request.session.get("cart", {})
    total_items = sum(item["quantity"] for item in cart.values()) if cart else 0
    return {"cart_total_items": total_items}