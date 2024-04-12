# we are creating the blog feeds for the users
import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New Post of My Blog'
    
    
    def items(self):
        return Post.published.all()[:5]
    
    def itemtitle(self,item):
        return item.title
    
    def item_description(self,item):
        return truncatewords_html(markdown.markdown(item.body),30)
    
    
    def item_pubdate(self,item):
        return item.publish