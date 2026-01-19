from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    """Afficher les items directement dans la page de commande"""
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 
                    'email', 'city', 'status', 'total_price', 'created_at']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['id', 'first_name', 'last_name', 'email']
    inlines = [OrderItemInline]
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informations utilisateur', {
            'fields': ('user', 'status')
        }),
        ('Informations de livraison', {
            'fields': ('first_name', 'last_name', 'email', 'address', 
                      'postal_code', 'city', 'phone')
        }),
        ('Informations de commande', {
            'fields': ('total_price', 'created_at', 'updated_at')
        }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity', 'get_cost']
    list_filter = ['order__created_at']
    search_fields = ['order__id', 'product__name']