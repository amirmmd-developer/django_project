from django.urls import path

from order.views import CheckoutView , PaymentSuccessView , PaymentFailedView

urlpatterns = [

    path('checkout/',CheckoutView.as_view()),

    path('payment/<int:payment_id>/success/',PaymentSuccessView.as_view()),

    path('payment/<int:payment_id>/failed/',PaymentFailedView.as_view()),

]