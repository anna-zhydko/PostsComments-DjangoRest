from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import NewsPost, Upvote, Comment
from .serializers import (
    NewsPostListSerializer,
    NewsPostDetailSerializer,
    CommentUpdateSerializer,
    CommentDetailSerializer,
    CreateVoteSerializer,
    NewsPostSerializer,
    CommentSerializer,
)
from .addition import get_ip
import datetime


class NewsPostListView(APIView):
    """Displays all newsposts from database"""

    def get(self, request):
        news_posts = NewsPost.objects.all()
        serializer = NewsPostListSerializer(news_posts, many=True)
        return Response(serializer.data)


class NewsPostDetailView(APIView):
    """Displays specified news post data"""

    def get(self, request, pk):
        news_post = get_object_or_404(NewsPost.objects.all(), pk=pk)
        serializer = NewsPostDetailSerializer(news_post)
        return Response(serializer.data)


class NewsPostUpdateView(APIView):
    """Updates specified news post"""

    def put(self, request, pk):
        news_post = get_object_or_404(NewsPost.objects.all(), pk=pk)
        serializer = NewsPostSerializer(news_post, data=request.data)
        if serializer.is_valid():
            serializer.save(creation_date=datetime.datetime.now().strftime("%Y-%m-%d"))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        news_post = get_object_or_404(NewsPost.objects.all(), pk=pk)
        news_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsPostCreateView(APIView):
    """Creates new news post"""

    def post(self, request):
        news_post = NewsPostSerializer(data=request.data)
        if news_post.is_valid():
            news_post.save(creation_date=datetime.datetime.now().strftime("%Y-%m-%d"))
        return Response(status=201)


class CommentListView(APIView):
    """Posts list output"""

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentCreateView(APIView):
    """Creates new comment"""

    def post(self, request):
        comment = CommentUpdateSerializer(data=request.data)
        if comment.is_valid():
            comment.save(creation_date=datetime.datetime.now().strftime("%Y-%m-%d"))
        return Response(status=201)


class CommentDetailView(APIView):
    """Displays specified comment data"""

    def get(self, request, pk):
        # news_post = NewsPost.objects.get(id=pk)
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        serializer = CommentDetailSerializer(comment)
        return Response(serializer.data)


class CommentUpdateView(APIView):
    """Updates specified comment"""

    def put(self, request, pk):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        serializer = CommentUpdateSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save(creation_date=datetime.datetime.now().strftime("%Y-%m-%d"))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpvoteView(APIView):
    """Allows upvote for specified news post"""

    def post(self, request):
        serializer = CreateVoteSerializer(data=request.data)
        ip = get_ip(request)
        last_vote_points = 0

        if serializer.is_valid():
            news_post_id = serializer.validated_data["news_post"]
            vote_points = serializer.validated_data["vote"]
            if vote_points in [1, -1]:

                upvote_object = Upvote.objects.filter(ip=ip)
                if upvote_object:
                    # the vote points before saving e.m if person already voted 1 or -1 it wouldn't change
                    last_vote_points = upvote_object[0].vote

                Upvote.objects.update_or_create(
                    ip=ip, news_post=news_post_id, defaults={"vote": vote_points}
                )

                news_post = NewsPost.objects.filter(pk=news_post_id.id)
                if (
                    last_vote_points != vote_points
                ):  # if client has changed the vote points
                    news_post.update(
                        amount_of_upvotes=news_post[0].amount_of_upvotes + vote_points
                    )

                return Response(status=201)
        return Response(status=400)
