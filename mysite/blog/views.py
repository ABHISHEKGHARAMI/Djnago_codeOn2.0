from django.shortcuts import render
from .models import Post
from django.http import Http404
# Create your views here.

# first view
def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {
            'posts':posts,
        }
    )

# 2nd view post detail
def post_detail(request,id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    
    return render(
        request,
        'blog/post/details.html',
        {
            'post' : post
        }
    )