from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from tinymce import HTMLField


class Category(models.Model):
    color = ColorField(default='#FFFFFF')
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.name

class Projects(models.Model):
    """
    Model for project/post by users
    """
    color = ColorField(default='#FFFFFF')
    category = models.ForeignKey('Category')
    is_sharable = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='Name')
    content = HTMLField('Content')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
