from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('', include('products.urls')),                     # home / product list
    path('cart/', include('cart.urls')),                   # <-- cart URLs
    path('orders/', include('orders.urls')),               # orders
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
