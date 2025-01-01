from django.db import models # type: ignore
from django.utils import timezone # type: ignore
from django.utils.text import slugify # type: ignore

# Create your models here.
class Article(models.Model):
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
