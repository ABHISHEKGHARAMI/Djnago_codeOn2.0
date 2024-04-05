from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    # post view
    #changing the post list view url for class based object .
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]