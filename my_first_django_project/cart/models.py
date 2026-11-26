from django.db import models

from django.conf import settings

class Cart(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE  , related_name='allusers' , related_query_name='alluserss')

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

class CartProducts(models.Model):

    cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name='allcarts' , related_query_name='allcartss')

    product = models.ForeignKey('products.Products' , on_delete=models.PROTECT , related_name='allproduts' , related_query_name='allproductss')

    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)