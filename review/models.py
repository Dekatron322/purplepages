from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app.models import App

# Create your models here.

class Review(models.Model):
    username = models.CharField(default="null", max_length=10)
    auth_code = models.TextField(default="null")

    detail = models.TextField(default="null")

    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.username)

