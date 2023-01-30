from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    caption = models.CharField(max_length=1000, default="null")
    price = models.CharField(max_length=1000, default="null")
    discount = models.CharField(max_length=1000, default="null")
    color = models.CharField(max_length=1000, default="null")

    status = models.BooleanField(default=False)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.caption)

