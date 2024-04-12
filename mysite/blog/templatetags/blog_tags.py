from django import template
from ..models import Post

# implementing the Count
from django.db.models import Count

# importing the markdown for the added filter
import markdown
# importing mark_safe
from django.utils.safestring import mark_safe


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
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


# adding the filter
@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))