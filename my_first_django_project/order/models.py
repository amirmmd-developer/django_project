from django.db import models

class Order(models.Model):

    class Status(models.TextChoices):

        PAID = 'pay' , 'its payed'

        CANCELED = 'canceled' , 'it canceled'

        FAILED = 'failed' , 'its failed'

        PENDING = 'pending' , 'its pending'

    user = models.ForeignKey('users.User' , on_delete=models.PROTECT , related_name='allusersssssssss' , related_query_name='allusersssssss')

    cart = models.OneToOneField(to='cart.Cart' , on_delete=models.PROTECT , related_name='allcartsssssssssssssssss' , related_query_name='allcartssssssssssssssssss')

    totla_price = models.DecimalField(max_digits=10 , decimal_places=5)

    status = models.CharField(choices=Status , default=Status.PENDING , max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):

    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='allordersss')

    product = models.ForeignKey('products.Products' , on_delete=models.PROTECT , related_name='itemsss' , related_query_name='itmessss')

    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    unit_price = models.DecimalField(max_digits=10 , decimal_places=5)

    @property

    def total_price(self):

        return self.unit_price * self.quantity

class Payment(models.Model):

    class Status(models.TextChoices):

        PAID = 'pay' , 'its payed'

        CANCELED = 'canceled' , 'it canceled'

        FAILED = 'failed' , 'its failed'

        PENDING = 'pending' , 'its pending'

    order = models.ForeignKey(Order , on_delete=models.PROTECT , related_name='allorderssssssss' , related_query_name='allorderssssssss')

    amount = models.DecimalField(max_digits=10 , decimal_places=5)

    status = models.CharField(choices=Status , default=Status.PENDING , max_length=10)