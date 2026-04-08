from rest_framework import serializers

from .models import Shop


# class ProductSerializer(serializers.ModelSerializer):
#     is_expensive = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#     def get_is_expensive(self, obj):
#         return obj.price > 1000
#
#     def validate_price(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Price manfiy bo'ladi")
#         return value
#
#     def validate(self, data):
#         if data['price'] > 10000:
#             raise serializers.ValidationError("Too expensive")
#         return data


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

    def perice1(self, p):
        if p < 0:
            return serializers.ValidationError("narx manfiy bolmaydi !")


    def price2(self, pk):
        if pk > 20000:
            raise serializers.ValidationError("narx juda qimmat bolmasligi kerak")
        return pk
