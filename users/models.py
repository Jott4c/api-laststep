from django.db import models
from django.contrib.auth.models import AbstractUser


class Types(models.TextChoices):
    CAREGIVER = "Cuidador"
    PATIENT = "Paciente"


class User(AbstractUser):
    age = models.DateField()
    phone = models.CharField(max_length=15)
    url_image = models.CharField(max_length=270, null=True)
    type = models.CharField(
        max_length=50,
        choices=Types.choices,
    )
    spec_or_cond = models.CharField(max_length=250, null=True)


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="address", null=True
    )
