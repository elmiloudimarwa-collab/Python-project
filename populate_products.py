import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
django.setup()

from products.models import Product

def populate():
    # Clear existing
    Product.objects.all().delete()
    
    products = [
        {
            'name': 'Smartphone X',
            'description': 'Latest smartphone with amazing features.',
            'price': 999.00,
            'image': 'products/smartphone.png'
        },
        {
            'name': 'Laptop Pro',
            'description': 'High performance laptop for professionals.',
            'price': 1499.50,
            'image': 'products/laptop.png'
        },
        {
            'name': 'Wireless Headphones',
            'description': 'Noise cancelling headphones for immersive sound.',
            'price': 199.99,
            'image': 'products/headphones.png'
        },
        {
            'name': 'Smart Watch',
            'description': 'Track your fitness and stay connected.',
            'price': 249.00,
            'image': 'products/smartwatch.png'
        }
    ]

    for p in products:
        Product.objects.create(
            name=p['name'],
            description=p['description'],
            price=p['price'],
            image=p['image']
        )
        print(f"Created product: {p['name']}")

if __name__ == '__main__':
    populate()
