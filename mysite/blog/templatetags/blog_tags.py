from django import template
from ..models import Post

# implementing the Count
from django.db.models import Count


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

# inclusion tags
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {
        'latest_posts' : latest_posts
    }
    
# simple tag
@register.simple_tag
def get_most_commented_post(count=5):
    return Post.published.annotate(
        total_comments=Count('comments').order_by('-total_comments')[:count]
    )