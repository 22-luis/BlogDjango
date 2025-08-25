from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.post import Post
from ..serializers.post import PostSerializer

class PostList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
