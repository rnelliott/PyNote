from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from tinymce import HTMLField

class Projects(models.Model):
    """
    Model for project/post by users
    """
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='Name')
    # content = models.TextField()
    content = HTMLField('Content')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.title
