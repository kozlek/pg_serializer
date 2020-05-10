import pg_serializer

from .models import User, Product, Order, OrderItem


class UserSerializer(pg_serializer.ModelSerializer):
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


class ProductSerializer(pg_serializer.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "ean", "title", "description", "unit_price", "materials")


class OrderSerializer(pg_serializer.ModelSerializer):
    buyer = pg_serializer.StringField(source="buyer__username")

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


class OrderItemSerializer(pg_serializer.ModelSerializer):
    order = pg_serializer.StringField(source="order__transaction_id")
    product = pg_serializer.StringField(source="product__ean")

    class Meta:
        model = OrderItem
        fields = ("order", "product", "quantity")
