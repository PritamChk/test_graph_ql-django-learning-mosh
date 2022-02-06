
from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    DateField,
    DecimalField,
    PositiveIntegerField,
    EmailField
)

T: bool = True  # True
F: bool = False  # False
STR_MAX_LENGTH: int = 255


class Product(Model):
    title: CharField = CharField(max_length=STR_MAX_LENGTH)
    description: TextField = TextField()
    price: DecimalField = DecimalField(max_digits=10, decimal_places=2)
    inventory: PositiveIntegerField = PositiveIntegerField()
    last_updated: DateTimeField = DateTimeField(auto_now=True)


class Customer(Model):
    
    __MEMBERSHIP_BRONZE__:str = "B"
    __MEMBERSHIP_SILVER__:str = "S"
    __MEMBERSHIP_GOLD__:str = "G"
    
    MEMBERSHIP_CHOICES = [
            (__MEMBERSHIP_BRONZE__,"Bronze"),
            (__MEMBERSHIP_SILVER__,"Silver"),
            (__MEMBERSHIP_GOLD__,"Gold")
        ]
    
    first_name: CharField = CharField(max_length=STR_MAX_LENGTH)
    last_name: CharField = CharField(max_length=STR_MAX_LENGTH)
    email: EmailField = EmailField(unique=T)
    phone: CharField = CharField(max_length=14, null=F)
    birth_date:DateField = DateField(null=T)
    membership : CharField = CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=__MEMBERSHIP_BRONZE__)


class Order(Model):
    PAYMENT_STATUS_PENDING = "P"    
    PAYMENT_STATUS_COMPLETE = "C"    
    PAYMENT_STATUS_FAILED = "F"
    
    PAYMENT_STATUS_CHOICES = [
            (PAYMENT_STATUS_COMPLETE,"Complete"),
            (PAYMENT_STATUS_PENDING,"Pending"),
            (PAYMENT_STATUS_FAILED,"Failed")
        ]    
    
    placed_at : DateTimeField = DateTimeField(auto_now_add=T)
    payment_status : CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)