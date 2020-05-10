import pytest

from .factories import UserFactory, ProductFactory, OrderFactory, OrderItemFactory


@pytest.fixture()
def users():
    return UserFactory.create_batch(size=10)


@pytest.fixture()
def products():
    return ProductFactory.create_batch(size=10)


@pytest.fixture()
def orders():
    return OrderFactory.create_batch(size=10)


@pytest.fixture()
def order_items():
    return OrderItemFactory.create_batch(size=10)
