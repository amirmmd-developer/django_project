from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from cart.serializer import CartSerializer , CartProductSerializer

from products.models import Products

from cart.models import Cart , CartProducts

class CartView(APIView):

    def get(self , request):

        serializer = CartSerializer(data = request.data)

        if serializer.is_valid():

            return Response(serializer.data)

class AddCartItems(APIView):

    def post(self , request):

        serializer = CartProductSerializer(data = request.data)

        if serializer.is_valid():

            product_name = serializer.validated_data('product_name')

            quantity = serializer.validated_data('quantity')

            product_find = Products.objects.filter(name = product_name).first()

            if product_find is None: 

                return Response({'eror':'product not found'} , status=status.HTTP_401_UNAUTHORIZED)

            cart_create = Cart.objects.get_or_create(user = request.user)

            if quantity <= Products.count:

                return Response({'eror':'not enough stock'} , status=status.HTTP_400_BAD_REQUEST)

            else:

                create_cart_product = CartProducts.objects.create(cart = cart_create , product = product_find , quantity = quantity)

                return Response({'message':'cart created'} , status=status.HTTP_201_CREATED)