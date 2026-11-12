from django.urls import path

from cart.views import AddCartItems , CartView

urlpatterns = [

    path('show/' , CartView.as_view()),

    path('add/' , AddCartItems.as_view()),

]