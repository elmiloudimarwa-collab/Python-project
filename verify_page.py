import os
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_site.settings')
django.setup()

def verify():
    c = Client()
    response = c.get('/')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        if "Smartphone X" in content and "Laptop Pro" in content:
            print("Verification SUCCESS: Products found in response.")
        else:
            print("Verification FAILED: Products NOT found in response.")
    else:
        print("Verification FAILED: Status code is not 200")

if __name__ == '__main__':
    verify()
