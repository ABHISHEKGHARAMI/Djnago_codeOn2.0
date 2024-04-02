from django.contrib import admin

# have to register the model to the admin for the user freindly interface to the admin site
from .models import Post
# Register your models here.

admin.site.register(Post)