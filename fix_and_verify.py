import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
django.setup()

from products.models import Product

count = Product.objects.count()
with open('count.txt', 'w') as f:
    f.write(str(count))
    
if count == 0:
    # Try to populate if empty
    print("Empty! Populating...")
    products = [
        {'name': 'Smartphone X', 'description': 'Feature phone', 'price': 999.00, 'image': 'products/smartphone.png'},
        {'name': 'Laptop', 'description': 'Fast laptop', 'price': 1500.00, 'image': 'products/laptop.png'}
    ]
    for p in products:
        Product.objects.create(**p)
    
    new_count = Product.objects.count()
    with open('count.txt', 'w') as f:
        f.write(str(new_count))
