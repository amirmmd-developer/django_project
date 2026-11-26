from django.urls import path

from cart.views import AddCartItems , GetCartItem

urlpatterns = [

    path('add/' , AddCartItems.as_view()),

    path('show/' , GetCartItem.as_view()),

]