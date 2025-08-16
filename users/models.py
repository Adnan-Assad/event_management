from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(r'^\+?\d{10,15}$', "Enter a valid phone number")]
    )
    profile_picture = models.ImageField(   
       
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username