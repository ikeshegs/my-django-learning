from django.db import models # type: ignore

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
