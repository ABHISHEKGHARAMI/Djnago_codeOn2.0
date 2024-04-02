from django.db import models
# importing time zone
from django.utils import timezone

# now time for creating  many  to one relationship for the model
from django.contrib.auth.models import User
# Create your models here.


# first we will create the Post model
class Post(models.Model):
    
    # here goes the char choice field for the status 
    # is it published or drafted
    class Status(models.TextChoices):
        DRAFT = 'DF','draft'
        PUBLISHED = 'PB','Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    #adding author
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    # adding the time field as the parameter of the model Post.
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # adding the status field for the model
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    # this will create enum like [('DF', 'draft'), ('PB', 'Published')] for status.
    
    
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
    
    
    #creation of the super user where username is - hunter001 password is : Suraj001@