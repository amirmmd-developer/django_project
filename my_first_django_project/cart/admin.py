from django.contrib import admin

from cart.models import Cart , CartProducts

admin.site.register(Cart)

admin.site.register(CartProducts)