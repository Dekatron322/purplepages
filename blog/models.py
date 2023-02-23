from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from app.models import App

# Create your models here.


class Comment(models.Model):
    commenter = models.ForeignKey(App, on_delete=models.CASCADE)
    comment = models.TextField(default="null")
    status = models.BooleanField(default=False)

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.comment)

class Blog(models.Model):
    image = models.FileField(upload_to='account_files/images/', blank=True, default="default_files/default_file.png")

    title = models.CharField(max_length=20, default="null")
    detail = models.TextField(default="null")
    status = models.BooleanField(default=False)

    tags = models.TextField(default="null")

    comments = models.ManyToManyField(Comment, through="BlogCommentConnector")

    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)



class BlogCommentConnector(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
