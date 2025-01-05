from django.db import models # type: ignore
from django.db.models.signals import pre_save, post_save  # type: ignore
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
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)
    # instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

post_save.connect(article_post_save, sender=Article)
