import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class User(AbstractUser):
    pass


class Product(models.Model):
    ean = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    materials = ArrayField(base_field=models.CharField(max_length=255))


class Order(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    transaction_time = models.DateTimeField()
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # delivery
    is_gift = models.BooleanField()
    shipping_date = models.DateField()
    # extra data
    additional_data = JSONField(default=dict)
    # M2M
    items = models.ManyToManyField(Product, through="OrderItem")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("order", "product"), name="order_product_unique"
            ),
        )
