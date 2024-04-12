# adding the sitemaps for search engine optimization
from django.contrib.sitemaps import Sitemap
from .models import Post

# class for the PostSitemap
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
def items(self):
    return Post.published.all()

def lastmod(self,obj):
    return obj.updated