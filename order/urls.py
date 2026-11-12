from django.urls import path

from order.views import OrderCreate

urlpatterns = [

    path('create_order/' , OrderCreate.as_view()),

]