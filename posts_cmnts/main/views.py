from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewsPost
from .serializers import NewsPostListSerializer, NewsPostDetailSerializer, CommentCreateSerializer


class NewsPostListView(APIView):
    """Posts list output"""
    def get(self, request):
        news_posts = NewsPost.objects.all()
        serializer = NewsPostListSerializer(news_posts, many=True)
        return Response(serializer.data)


class NewsPostDetailView(APIView):

    def get(self, request, pk):
        news_post = NewsPost.objects.get(id=pk)
        serializer = NewsPostDetailSerializer(news_post)

        return Response(serializer.data)


class CommentCreateView(APIView):

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)
