from django.contrib import admin
from django.urls import path, include

import Blog

urlpatterns = [
    path('blog/', include("Blog.urls")),
    path('admin/', admin.site.urls)
]
