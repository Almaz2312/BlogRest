from rest_framework import views, status
from rest_framework.response import Response

from post.models import Post
from post.serializers import PostSerializer


class PostAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
