from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns =[
    # post view
    #changing the post list view url for class based object .
    path('',views.post_list,name='post_list'),
    path('tag/<slug:tag_slug>/',
         views.post_list,name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    # adding the share url
    path('<int:post_id>/share',views.post_share,
         name= "post_share"),
    path('<int:post_id>/comment/',
         views.post_comments,
         name='post_comments'),
    path('/feeds',LatestPostsFeed(),name="post_feed"),
]