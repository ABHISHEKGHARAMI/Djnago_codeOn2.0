from django.shortcuts import render , get_object_or_404
from .models import Post
from django.http import Http404
#adding the paginator
from django.core.paginator import Paginator
# Create your views here.

# first view
def post_list(request):
    post_list = Post.published.all()
    #print(posts)
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)
    posts = paginator.page(page_number)
    return render(
        request,
        'blog/post/list.html',
        {
            'posts':posts,
        }
    )

# 2nd view post detail
def post_detail(request,year,month,day,post):
    '''try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')'''
    #can do same thing with the help of the get_object_or_404
    
    post = get_object_or_404(
        Post,
        status = Post.Status.PUBLISHED,
        slug = post,
        publish__year = year,
        publish__month = month,
        publish__day = day
    )
    
    return render(
        request,
        'blog/post/detail.html',
        {
            'post' : post
        }
    )