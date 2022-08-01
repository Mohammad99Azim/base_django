from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    phone_number = models.CharField(default="+999999999", validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.username
