from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=20, default="null")
    detail = models.TextField(default="null")

    status = models.BooleanField(default=False)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)


