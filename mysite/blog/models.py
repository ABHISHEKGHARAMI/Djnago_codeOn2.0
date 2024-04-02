from django.db import models

# Create your models here.


# first we will create the Post model
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    
    # method for title
    def __str__(self):
        return self.title