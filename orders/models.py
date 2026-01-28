from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    """Modèle pour une commande"""
    
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('processing', 'En traitement'),
        ('paid', 'Payée'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name="Adresse")
    postal_code = models.CharField(max_length=20, verbose_name="Code postal")
    city = models.CharField(max_length=100, verbose_name="Ville")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name="Statut"
    )
    
    total_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Prix total"
    )
    
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Carte bancaire'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('paid', 'Payé'),
        ('failed', 'Échoué'),
    ]
    
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='card',
        verbose_name="Méthode de paiement"
    )
    
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending',
        verbose_name="Statut du paiement"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
    
    def __str__(self):
        return f"Commande #{self.id} - {self.user.username}"
    
    def get_total_cost(self):
        """Calcule le coût total de la commande"""
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Modèle pour un article dans une commande"""
    
    order = models.ForeignKey(
        Order, 
        related_name='items', 
        on_delete=models.CASCADE,
        verbose_name="Commande"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        verbose_name="Produit"
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Prix unitaire"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    
    class Meta:
        verbose_name = "Article de commande"
        verbose_name_plural = "Articles de commande"
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    def get_cost(self):
        """Calcule le coût total de cet article"""
        return self.price * self.quantity