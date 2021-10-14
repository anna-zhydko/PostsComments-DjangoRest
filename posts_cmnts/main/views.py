from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404

from .models import NewsPost, Upvote
from .serializers import NewsPostListSerializer, NewsPostDetailSerializer, CommentCreateSerializer, \
    CreateVoteSerializer, NewsPostSerializer
from .addition import get_ip
import datetime


class NewsPostListView(APIView):
    """Posts list output"""
    def get(self, request):
        news_posts = NewsPost.objects.all()
        serializer = NewsPostListSerializer(news_posts, many=True)
        return Response(serializer.data)


class NewsPostDetailView(APIView):

    def get(self, request, pk):
        # news_post = NewsPost.objects.get(id=pk)
        news_post = get_object_or_404(NewsPost.objects.all(), pk=pk)
        serializer = NewsPostDetailSerializer(news_post)
        return Response(serializer.data)


class NewsPostUpdateView(APIView):

    def put(self, request, pk):
        # news_post = NewsPost.objects.get(id=pk)
        news_post = get_object_or_404(NewsPost.objects.all(), pk=pk)
        serializer = NewsPostSerializer(news_post, data=request.data)
        if serializer.is_valid():
            serializer.save(creation_date=datetime.datetime.now().strftime('%Y-%m-%d'))
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # news_post = NewsPost.objects.get(id=pk)
        news_post = get_object_or_404(NewsPost.objects.all(), pk=pk)
        news_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsPostCreateView(APIView):

    def post(self, request):
        news_post = NewsPostSerializer(data=request.data)
        if news_post.is_valid():
            news_post.save(creation_date=datetime.datetime.now().strftime('%Y-%m-%d'))
        return Response(status=201)


class CommentCreateView(APIView):

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save(creation_date=datetime.datetime.now().strftime('%Y-%m-%d'))
        return Response(status=201)


class UpvoteView(APIView):

    def post(self, request):
        serializer = CreateVoteSerializer(data=request.data)
        if serializer.is_valid():
            news_post_id = serializer.validated_data['news_post'].id
            vote_points = serializer.validated_data['vote']
            ip = get_ip(request)

            last_vote_points = Upvote.objects.filter(ip=ip)[0].vote  # the vote points before saving

            serializer.save(ip=ip)

            news_post = NewsPost.objects.filter(pk=news_post_id)
            if last_vote_points != vote_points:  # if client has changed the vote points
                news_post.update(amount_of_upvotes=news_post[0].amount_of_upvotes + vote_points)
            return Response(status=201)
        else:
            return Response(status=400)
