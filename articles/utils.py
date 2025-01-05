import random

from django.utils.text import slugify # type: ignore

def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id) # qs = QuerySets

    if qs.exists():
        # auto generates new slug
        rand_int = random.randint(300_000, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, new_slug=slug)

    instance.slug = slug

    if save:
        instance.save()