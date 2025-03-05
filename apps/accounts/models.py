from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and returns a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)  # Atribuindo o email ao campo username

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Role(models.TextChoices):
    MANAGER = "Manager", "Manager"
    EMPLOYEE = "Employee", "Employee"
    CUSTOMER = "Customer", "Customer"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # O 'email' será o identificador único

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    phone_number = models.CharField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = 'email'  # Define o email como o campo de login
    REQUIRED_FIELDS = []  # Não será necessário o 'username' na criação do superusuário

    objects = CustomUserManager()

    def __str__(self):
        return self.email
