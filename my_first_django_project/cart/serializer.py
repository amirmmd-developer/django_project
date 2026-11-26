from rest_framework import serializers

from cart.models import Cart , CartProducts

class CartSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cart

        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):

    produnt_name = serializers.CharField()

    quantity = serializers.IntegerField()

    class Meta:

        model = CartProducts

        fields = '__all__'