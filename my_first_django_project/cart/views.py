from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from cart.services import add_to_cart , get_active_cart

from rest_framework.permissions import IsAuthenticated

from cart.serializer import CartSerializer

class AddCartItems(APIView):

    permission_classes = [IsAuthenticated]

    def post(self , request , *args , **kwargs):

        user = request.user

        product = request.data['product_id']

        quantity = request.data['quantity']

        cartirem = add_to_cart(user=user , quantity=quantity , product_id=product)

        return Response({'data':cartirem.id} , status=status.HTTP_201_CREATED)
    
class GetCartItem(APIView):

    permission_classes = [IsAuthenticated]

    def get(self , request , *args , **kwargs):

        cart = get_active_cart(request.user)

        serializer = CartSerializer(cart)

        return Response({'data': serializer.data},status=status.HTTP_200_OK)