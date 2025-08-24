from django.urls import path
from Blog.views import post

app_name = 'blog'
urlpatterns = [
    path("", post.index, name='index'),
    path("<int:post_id>/", post.detail, name='detail')
]
