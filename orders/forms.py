from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    """Formulaire pour créer une commande"""
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 
                  'postal_code', 'city', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '123 Rue Exemple'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10000'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rabat'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+212 6XX XXX XXX'
            }),
        }