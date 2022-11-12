from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.fields import CharField
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_id')
    # username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_username')
    title = models.CharField(max_length=264, verbose_name="Title")
    article = models.TextField(verbose_name="Description")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    Private = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
