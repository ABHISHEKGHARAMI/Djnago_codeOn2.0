from django.db import models
# importing time zone
from django.utils import timezone
# Create your models here.


# first we will create the Post model
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    # adding the time field as the parameter of the model Post.
    publish = models.TimeField(default=timezone.now)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    
    
    # basically what happens is the posts to be shown in the website should be reverse order
    # like newer post are first then the older post
    # thats why we are creating the meta data of the model 
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    # method for title
    def __str__(self):
        return self.title