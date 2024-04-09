from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from django.http import Http404
#adding the paginator
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
# Create your views here.
from django.views.generic import ListView

# adding   the form in view
from .forms import EmailPostForm , CommentForm
# adding the send mail module from django
from django.core.mail import send_mail

# from django.decorater we will use the post method
from django.views.decorators.http import require_POST

# importing the django.taggit
from taggit.models import Tag

# from django importing models agrresgation
from django.db.models import Count
# first view
def post_list(request,tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    #print(posts)
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(num_pages)
    return render(
        request,
        'blog/post/list.html',
        {
            'posts':posts,
            'tag':tag
        }
    )
# Adding the post list view
class PostListView(ListView):
    # adding the class based post_list function
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

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
    comments = post.comments.filter(active=True)
    form = CommentForm()
    
    # adding the similar post excluding the post
    post_tag_ids = post.tags.values_list('id',
                                         flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags = Count('tags')).order_by(['-same_tags',
                                                                                '-publish'])[:4]
    
    
    return render(
        request,
        'blog/post/detail.html',
        {
            'post' : post,
            'comments' : comments,
            'form' : form ,
            'similar_posts' : similar_posts
        }
    )
    
    
# creating the view function for the form
def post_share(request,post_id):
    # retrive the post using the post_id
    post = get_object_or_404(
        Post,
        id = post_id,
        status = Post.Status.PUBLISHED
    )
    sent = False
    
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recommends you read " \
                f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'your_account@gmail.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    
    
    # rendering
    return render(request,
                  'blog/post/share.html',
                  {
                      'post':post,
                      'form':form,
                      'sent':sent
                  }
                  )
    
# for method
@require_POST
def post_comments(request,post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status = Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render('blog/post/comment.html',
                  {
                      'post':post,
                      'form':form,
                      'comment':comment
                  })