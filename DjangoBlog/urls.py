from django.contrib import admin
from django.urls import path, include

from Blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('Blog.urls', namespace='blog')),
]
