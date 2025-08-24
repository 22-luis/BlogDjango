from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from Blog.models import Post


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by("date")[:5]
    context = {"latest_post_list": latest_post_list}
    return render(request, "blog/index.html", context)

def detail(request, post_id):
    post  = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/detail.html", {"post": post})

def content(request, post_id):
    response = "You are looking at task %s."
    return HttpResponse(response % post_id)