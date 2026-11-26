from order.models import Order , OrderItem , Payment

from cart.models import CartProducts , Cart

from products.models import Products

from django.db import transaction

def get_payment(payment_id):
    
    payment = Payment.objects.get(id = payment_id)

    if not payment:

        raise ValueError('....')

    return payment

def crate_checkout(user):

    cart = Cart.objects.get(user=user , is_active = True)

    if not cart:

        raise ValueError('....')

    cart_item = CartProducts.objects.filter(cart=cart)

    if not cart_item.exists():

        raise ValueError('....')

    total_price = sum(

        item.product.price * item.quantity

        for item in cart_item

    )

    order = Order.objects.create(user = user , total_price = total_price , cart =  cart)

    cart_itemss = []

    for order_item in cart_item:

        cart_itemss.append(OrderItem(order = order , product = order_item.product , unit_price = order_item.product.price , quantity = order_item.quantity))

    OrderItem.objects.bulk_create(cart_itemss)

    payment = Payment.objects.create(amount = total_price , order = order)

    return payment

def payment_suucced(payment_id):

    payment = get_payment(payment_id)

    with transaction.atomic():

        payment.status = Payment.Status.PAID

        payment.save(update_fields=['status'])

        order = payment.order

        order.status = Payment.Status.PAID

        payment.save(update_fields=['status'])

        decrease_product_count(cart)

        cart = order.cart

        cart.is_active = False

        cart.save(update_fields=['is_active'])

def payment_faield(payment_id):

    with transaction.atomic():

        payment = get_payment(payment_id)

        payment.status = Payment.Status.FAILED

        payment.save(update_fields=['status'])

        order = payment.order

        order.status = Order.Status.FAILED

        order.save(update_fields=['status'])

    return payment , order

def decrease_product_count(cart):

    cart_item = CartProducts.objects.filter(cart=cart)

    for item in cart_item:

        product = Products.objects.select_for_update().get(id=item.product_id)

        product.count -= item.quantity

        product.save()