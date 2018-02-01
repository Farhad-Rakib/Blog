from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from djrichtextfield.models import RichTextField


# Create your models here.

class Post(models.Model):
    
    STATUS_CHOICES = (
       ("draft","Draft"),
       ("published","Publish"),

    )
    categories = models.ManyToManyField('Category',blank=True)
    author = models.ForeignKey(User,related_name="blog_posts")
    title = models.CharField(max_length=250)
    content = RichTextField()
    status = models.CharField(max_length = 15,
                                choices = STATUS_CHOICES,
                                default="draft")
    published = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title;


class Category(models.Model):

    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(blank=True,unique = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name