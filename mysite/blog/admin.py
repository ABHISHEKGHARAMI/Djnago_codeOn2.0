from django.contrib import admin

# have to register the model to the admin for the user freindly interface to the admin site
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # this is for what to display in the post 
    list_display = ['title','slug','author','publish','status']
    # this is for the filtering purpose to the post
    list_filter = ['status','created','publish','author']
    # for searching purpose
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author'] 
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created','active']
    list_filter = ['created','updated','active']
    search_fields = ['name','email','body']
    