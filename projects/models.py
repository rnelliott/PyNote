from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Projects(models.Model):
    """
    Model for project/post by users
    """
    author = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=200)
    # content = models.TextField()
    content = RichTextField(config_name='awesome_ckeditor')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __unicode__(self):
        return self.title
