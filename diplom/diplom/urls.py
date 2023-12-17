from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^cart/', include('cart.urls')),
    re_path(r'^orders/', include('orders.urls')),
    re_path(r'^', include('shop.urls')),
]
