from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class App(models.Model):
    image = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_code = models.TextField(default="null")

    first_name = models.CharField(max_length=20, default="null")
    last_name = models.CharField(max_length=20, default="null")
    phone = models.CharField(max_length=20, default="null")

    otp_code = models.TextField(default="null")
    status = models.BooleanField(default=False)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.username)


