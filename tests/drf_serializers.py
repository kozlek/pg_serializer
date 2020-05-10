from rest_framework import serializers

from .models import User, Product, Order, OrderItem


class ConsistentIsoDatetimeField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.isoformat(timespec="microseconds")


class UserSerializer(serializers.ModelSerializer):
    date_joined = ConsistentIsoDatetimeField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "date_joined",
        )


class ProductSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Product
        fields = ("id", "ean", "title", "description", "unit_price", "materials")


class OrderSerializer(serializers.ModelSerializer):
    transaction_time = ConsistentIsoDatetimeField()
    buyer = serializers.CharField(source="buyer.username")

    class Meta:
        model = Order
        fields = (
            "transaction_id",
            "transaction_time",
            "buyer",
            "is_gift",
            "shipping_date",
            "additional_data",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.CharField(source="order.transaction_id")
    product = serializers.CharField(source="product.ean")

    class Meta:
        model = OrderItem
        fields = ("order", "product", "quantity")
