from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app.models import App
from product.models import Product
# Create your models here.


class Wishlist(models.Model):
    owner = models.ForeignKey(App, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    status = models.BooleanField(default=False)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.owner.user)

