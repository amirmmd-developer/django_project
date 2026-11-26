from rest_framework import serializers

from order.models import Order , OrderItem

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderItem

        fields = ['product','quantity','unit_price']

class OrderSeializer(serializers.ModelSerializer):

    allorders = OrderItemSerializer(many=True, read_only=True)

    class Meta:

        model = Order

        fields = ['total_price', 'status', 'items']