from rest_framework import serializers
from .models import NewsPost, Comment


class NewsPostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsPost
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class NewsPostDetailSerializer(serializers.ModelSerializer):
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = NewsPost
        fields = '__all__'