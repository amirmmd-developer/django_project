from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from order.serializer import OrderItemSerializer , OrderSeializer

from order.models import Order , OrderItem

from cart.models import Cart

class OrderCreate(APIView):

    def post(self , request):

        cart = Cart.objects.filter(user = request.user)

        items = cart.allcarts.all()

        if not items.exists():

            return Response({'eror':'cart is not indigits'} , status=status.HTTP_400_BAD_REQUEST)

        total = 0

        for i in items:

            total += items.product.price * items.quantity

        order = Order.objects.create(user = request.user , total_price = total)

        for j in items:

            OrderItem.objects.create(order=order , product=items.product , quantity=items.quantity , unit_price=items.product.price)

            return Response({'message','order created'} , status=status.HTTP_201_CREATED)