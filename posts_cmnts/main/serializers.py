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


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('author_name', 'content', 'creation_date', 'parent_comment')


class NewsPostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = NewsPost
        fields = '__all__'
