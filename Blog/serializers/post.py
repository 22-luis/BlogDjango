from rest_framework import serializers

from Blog.models.post import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description','content','date']