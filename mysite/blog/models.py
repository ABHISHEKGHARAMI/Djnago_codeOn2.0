from django.db import models
# importing time zone
from django.utils import timezone

# now time for creating  many  to one relationship for the model
from django.contrib.auth.models import User
# for creating the canonical url we will use reverse method
from django.urls import reverse
# Create your models here.

# adding the django-taggit system  for tagging to the posts
from taggit.managers import TaggableManager

# custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
# first we will create the Post model
class Post(models.Model):
    
    # here goes the char choice field for the status 
    # is it published or drafted
    class Status(models.TextChoices):
        DRAFT = 'DF','draft'
        PUBLISHED = 'PB','Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique='publish')
    #adding author
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    # adding the time field as the parameter of the model Post.
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    tags = TaggableManager()
    
    # adding the status field for the model
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    
    # declaring the managers
    objects = models.Manager() # default manager
    published = PublishedManager() # custom manager
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
    
    # for dynamically build url
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,
                                                self.publish.month,
                                                self.publish.day,
                                                self.slug
                                                ])
    
    #creation of the super user where username is - hunter001 password is : Suraj001@
    
    
# creating the comment model
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    # creating the meta class
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        
    def __str__(self):
        return f"commented by {self.name} on {self.post}"