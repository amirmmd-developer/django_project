from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from rest_framework import status

from order.services import crate_checkout , payment_suucced , payment_faield

from cart.models import Cart

from order.models import Payment

class CheckoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        payment = crate_checkout(request.user)

        return Response({'payment_id': payment.id,'amount': payment.amount,'status': payment.status},status=status.HTTP_201_CREATED)

class PaymentSuccessView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, payment_id):

        payment = Payment.objects.get(id=payment_id,order__user=request.user)


        payment_suucced(payment_id)

        return Response({'message': 'payment succeeded'},status=status.HTTP_200_OK)

class PaymentFailedView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, payment_id):

        payment = Payment.objects.get(id=payment_id,order__user=request.user)

        payment_faield(payment_id)

        return Response({'message': 'payment failed'},status=status.HTTP_200_OK)