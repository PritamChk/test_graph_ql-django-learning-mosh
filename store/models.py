
from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    DateField,
    DecimalField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    EmailField
)

# ---------------------------------------------

from django.db.models import (
    OneToOneField,
    ManyToManyField,
    ForeignKey,
    CASCADE,
    PROTECT
)

# -----------------------------------------------

T: bool = True  # True
F: bool = False  # False
STR_MAX_LENGTH: int = 255

# _________________________________________________


class Collection(Model):
    title: CharField = CharField(max_length=STR_MAX_LENGTH)


class Product(Model):
    title: CharField = CharField(max_length=STR_MAX_LENGTH)
    description: TextField = TextField()
    price: DecimalField = DecimalField(max_digits=10, decimal_places=2)
    inventory: PositiveIntegerField = PositiveIntegerField()
    last_updated: DateTimeField = DateTimeField(auto_now=True)
    collection = ForeignKey(Collection, on_delete=PROTECT)


class Customer(Model):

    __MEMBERSHIP_BRONZE__: str = "B"
    __MEMBERSHIP_SILVER__: str = "S"
    __MEMBERSHIP_GOLD__: str = "G"

    MEMBERSHIP_CHOICES = [
        (__MEMBERSHIP_BRONZE__, "Bronze"),
        (__MEMBERSHIP_SILVER__, "Silver"),
        (__MEMBERSHIP_GOLD__, "Gold")
    ]

    first_name: CharField = CharField(max_length=STR_MAX_LENGTH)
    last_name: CharField = CharField(max_length=STR_MAX_LENGTH)
    email: EmailField = EmailField(unique=T)
    phone: CharField = CharField(max_length=14, null=F)
    birth_date: DateField = DateField(null=T)
    membership: CharField = CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=__MEMBERSHIP_BRONZE__)


class Address(Model):
    address_details: TextField = TextField()
    zip: CharField = CharField(max_length=10, null=True)
    customer = OneToOneField("Customer", on_delete=CASCADE, primary_key=True)


class Order(Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_FAILED, "Failed")
    ]

    placed_at: DateTimeField = DateTimeField(auto_now_add=T)
    payment_status: CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = ForeignKey("Customer", on_delete=PROTECT)


class OrderItem(Model):
    order = ForeignKey("Order", on_delete=PROTECT)
    product = ForeignKey("Porduct", on_delete=PROTECT)
    quantity = PositiveSmallIntegerField()
    unit_cost = DecimalField(max_digits=10, decimal_places=2)


class Cart(Model):
    created_at: DateTimeField = DateTimeField(auto_now_add=T)


class CartItems(Model):
    cart = ForeignKey("Cart", on_delete=CASCADE)
    product = ForeignKey("Product", on_delete=CASCADE)
    quantity = PositiveSmallIntegerField()
