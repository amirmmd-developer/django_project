from products.models import Products

from django.db import transaction

from cart.models import Cart , CartProducts

def get_active_cart(user):

    cart = Cart.objects.get(user = user , is_active = True)

    if not cart:

        raise ValueError('....')

    return cart

@transaction.atomic

def add_to_cart(user, product_id, quantity):

    product = Products.objects.get(id=product_id)

    if quantity <= 0 or quantity > product.count:

        raise ValueError('....')

    cart, created = Cart.objects.get_or_create(user=user,is_active=True)

    cart_item, created = CartProducts.objects.get_or_create(cart=cart,product=product,defaults={'quantity': quantity})

    if not created:

        new_quantity = cart_item.quantity + quantity

        if new_quantity > product.count:

            raise ValueError('....')

        cart_item.quantity = new_quantity

        cart_item.save()

    return cart_item