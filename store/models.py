from re import search
from django.core.validators import MinValueValidator

from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    DateField,
    DecimalField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    EmailField,SlugField
)

# ---------------------------------------------

from django.db.models import (
    OneToOneField,
    ManyToManyField,
    ForeignKey,
    CASCADE,
    PROTECT,
    SET_NULL
)

from django.db.models import Index
# from django.forms import SlugField
# -----------------------------------------------

T: bool = True  # True
F: bool = False  # False
STR_MAX_LENGTH: int = 300

# _________________________________________________


class Collection(Model):
    title: CharField = CharField(max_length=STR_MAX_LENGTH)
    featured_products = ForeignKey("Product", on_delete=SET_NULL, null=T,related_name="+",blank=T)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["title"]
        


class Promotion(Model):
    description = CharField(max_length=STR_MAX_LENGTH)
    discount: DecimalField = DecimalField(
        max_digits=4, decimal_places=1)


    
class Product(Model):
    slug = SlugField(max_length=STR_MAX_LENGTH)
    title: CharField = CharField(max_length=STR_MAX_LENGTH)
    description: TextField = TextField(null=T,blank=T)
    price: DecimalField = DecimalField(max_digits=10, decimal_places=2, 
                                       validators=[MinValueValidator(0)])
    inventory: PositiveIntegerField = PositiveIntegerField()
    last_update: DateTimeField = DateTimeField(auto_now=True)
    collection = ForeignKey(Collection, on_delete=PROTECT,null=T)
    promotions = ManyToManyField("Promotion",blank=True)
    # 
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["title","price","inventory"]


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
    birth_date: DateField = DateField(null=True,blank=T)
    membership: CharField = CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=__MEMBERSHIP_BRONZE__)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        indexes = [Index(fields=[
                "first_name",
                "last_name"
            ])]

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
    payment_status:CharField = CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = ForeignKey("Customer", on_delete=PROTECT)


class OrderItem(Model):
    order = ForeignKey("Order", on_delete=PROTECT)
    product = ForeignKey("Product", on_delete=PROTECT)
    quantity = PositiveSmallIntegerField()
    unit_cost = DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"order_id : {self.id} || Product Price : {self.product.price}"


class Cart(Model):
    created_at: DateTimeField = DateTimeField(auto_now_add=T)

    def __str__(self) -> str:
        return f"{self.id} - created at : {self.created_at.date()}"

class CartItems(Model):
    cart = ForeignKey("Cart", on_delete=CASCADE)
    product = ForeignKey("Product", on_delete=CASCADE)
    quantity = PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.product.title