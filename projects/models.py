from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from colorfield.fields import ColorField

import uuid

class Category(models.Model):
    color = ColorField(default='#FF0000')
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.name

class Projects(models.Model):
    """
    Model for project/post by users
    """
    # Create unique-sharable ID
    # uuid = uuid.uuid4()
    # uuid = models.CharField(max_length=64, default=uuid, unique=True)
    color = ColorField(default='#FF0000')
    category = models.ForeignKey('Category')
    is_sharable = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='Name')
    # content = models.TextField()
    content = HTMLField('Content')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title
