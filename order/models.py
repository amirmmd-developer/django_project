from django.db import models

class Order(models.Model):

    class Status(models.TextChoices):

        PAY = 'pay' , 'its payed'

        CANCELED = 'canceled' , 'it canceled'

        PENDING = 'pending' , 'its pending'

    user = models.ForeignKey('users.User' , on_delete=models.PROTECT)

    totla_price = models.DecimalField()

    status = models.CharField(choices=Status , default=Status.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):

    order = models.ForeignKey(Order , on_delete=models.CASCADE)

    product = models.ForeignKey('products.Products' , on_delete=models.PROTECT , related_name='items')

    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    unit_price = models.DecimalField()