from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Link(models.Model):
    Target_url = models.URLField(max_length=200)
    Description = models.CharField(max_length=200)
    Identifier = models.SlugField(blank=True, unique=True, max_length=20)
    Author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts")
    Created_date = models.DateTimeField(auto_now= True)
    Active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return self.identifier