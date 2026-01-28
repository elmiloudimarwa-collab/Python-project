from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    """Formulaire pour créer une commande"""
    
    # Mock credit card fields (not processed, just for UI)
    card_number = forms.CharField(
        max_length=19,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '1234 5678 9012 3456',
            'pattern': '[0-9 ]+',
        }),
        label="Numéro de carte"
    )
    
    card_expiry = forms.CharField(
        max_length=5,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/YY',
            'pattern': '[0-9]{2}/[0-9]{2}',
        }),
        label="Date d'expiration"
    )
    
    card_cvv = forms.CharField(
        max_length=3,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '123',
            'pattern': '[0-9]{3}',
        }),
        label="CVV"
    )
    
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