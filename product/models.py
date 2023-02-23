from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    image = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")
    
    caption = models.CharField(max_length=100, default="null")
    price = models.CharField(max_length=100, default="null")
    discount = models.CharField(max_length=100, default="null")
    color = models.CharField(max_length=100, default="null")

    status = models.BooleanField(default=False)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.caption)

