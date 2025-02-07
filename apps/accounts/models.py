from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    MANAGER = "Manager", "Manager"
    EMPLOYEE = "Employee", "Employee"
    CUSTOMER = "Customer", "Customer"

class CustomUser(AbstractUser):
    
    username = None
    email = models.EmailField( unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email
