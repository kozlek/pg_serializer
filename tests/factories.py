from datetime import timedelta

import factory
import pytz

from .models import User, Product, Order, OrderItem


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.LazyAttribute(
        lambda o: o.username + "@" + factory.Faker("free_email_domain").generate()
    )
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = User
        django_get_or_create = ("username",)


class ProductFactory(factory.django.DjangoModelFactory):
    ean = factory.Faker("ean")
    title = factory.Faker("text", max_nb_chars=25)
    description = factory.Faker("paragraph")
    unit_price = factory.Faker("pydecimal", positive=True, min_value=1, max_value=999)
    materials = factory.Faker("words")

    class Meta:
        model = Product
        django_get_or_create = ("ean",)


class OrderFactory(factory.django.DjangoModelFactory):
    transaction_id = factory.Faker("uuid4")
    transaction_time = factory.Faker("date_time", tzinfo=pytz.UTC)
    buyer = factory.SubFactory(UserFactory)
    # delivery
    is_gift = factory.Faker("pybool")
    shipping_date = factory.LazyAttribute(
        lambda o: factory.Faker(
            "date_between_dates",
            date_start=(o.transaction_time + timedelta(days=1)),
            date_end=(o.transaction_time + timedelta(days=7)),
        ).generate()
    )
    # extra data
    # TODO: re-enable ObjectField tests after figure out the ": " separator issue
    # additional_data = factory.Faker("pydict", value_types=("str", "float", "int"),)

    class Meta:
        model = Order
        django_get_or_create = ("transaction_id",)


class OrderItemFactory(factory.django.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint", min_value=1, max_value=99)

    class Meta:
        model = OrderItem
        django_get_or_create = ("order", "product")
