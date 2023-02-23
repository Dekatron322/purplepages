from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app.models import App
from product.models import Product
from service.models import Service
from blog.models import Blog
from review.models import Review

# Create your models here.

class Business(models.Model):
    app_user = models.ForeignKey(App, on_delete=models.CASCADE)
    auth_code = models.TextField(default="null")

    image = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    name = models.CharField(max_length=50, default="null")
    business_type = models.CharField(max_length=50, default="null")
    rc_number = models.CharField(max_length=50, default="null")
    category = models.CharField(max_length=50, default="null")
    location = models.CharField(max_length=50, default="null")
    description = models.TextField(default="null")
    email = models.CharField(max_length=50, default="null")
    phone = models.CharField(max_length=50, default="null")
    website = models.CharField(max_length=50, default="null")
    address = models.TextField(default="null")
    marketplace = models.CharField(max_length=50, default="null")
    marketplace_link = models.CharField(max_length=50, default="null")

    rating = models.CharField(max_length=10, default="0")

    products = models.ManyToManyField(Product, through="BusinessProductConnector")
    services = models.ManyToManyField(Service, through="BusinessServiceConnector")
    blogs = models.ManyToManyField(Blog, through="BusinessBlogConnector")

    reviews = models.ManyToManyField(Review, through="BusinessReviewConnector")

    promoted = models.BooleanField(default=False)

    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)



class BusinessReviewConnector(models.Model):
	business = models.ForeignKey(Business, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class BusinessProductConnector(models.Model):
	business = models.ForeignKey(Business, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class BusinessServiceConnector(models.Model):
	business = models.ForeignKey(Business, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)

class BusinessBlogConnector(models.Model):
	business = models.ForeignKey(Business, on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)