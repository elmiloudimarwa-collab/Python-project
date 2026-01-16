from django.db import models
from django.contrib.auth.models import User
from products.models import Product



class Order(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Nouvelle'),
        ('PAID', 'Payée'),
        ('SHIPPED', 'Expédiée'),
        ('CANCELLED', 'Annulée'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')

    def __str__(self):
        return f"Commande #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} x {self.quantity}"
