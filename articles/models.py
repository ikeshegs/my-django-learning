from django.db import models # type: ignore
from django.utils import timezone # type: ignore

# Create your models here.
class Article(models.Model):
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
