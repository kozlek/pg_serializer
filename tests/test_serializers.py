import json

import pytest
from django.db import connection
from rest_framework.utils.encoders import JSONEncoder

from . import drf_serializers
from .models import User, Product, Order, OrderItem
from .serializers import (
    UserSerializer,
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer,
)

pytestmark = pytest.mark.django_db


def json_encode(data):
    return json.dumps(data, cls=JSONEncoder, separators=(",", ":")).encode(
        connection.connection.encoding
    )


def test_serialize_users(users):
    pg_result = UserSerializer(queryset=User.objects.all(), as_bytes=True).json
    drf_result = json_encode(
        drf_serializers.UserSerializer(User.objects.all(), many=True).data
    )
    assert pg_result == drf_result


def test_serialize_products(products):
    pg_result = ProductSerializer(queryset=Product.objects.all(), as_bytes=True).json
    drf_result = json_encode(
        drf_serializers.ProductSerializer(Product.objects.all(), many=True).data
    )
    assert pg_result == drf_result


def test_serialize_orders(orders):
    pg_result = OrderSerializer(queryset=Order.objects.all(), as_bytes=True).json
    drf_result = json_encode(
        drf_serializers.OrderSerializer(Order.objects.all(), many=True).data
    )
    assert pg_result == drf_result


def test_serialize_no_data():
    pg_result = OrderSerializer(queryset=Order.objects.all(), as_bytes=True).json
    assert pg_result == b"[]"
