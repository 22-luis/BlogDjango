from django.urls import path
from Blog.views.post import PostList

app_name = 'blog'
urlpatterns = [
    path("post/", PostList.as_view(), name='post_get_all'),
]
