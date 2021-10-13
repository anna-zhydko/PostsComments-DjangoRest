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


class FilterCommentSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent_comment=None)
        return super().to_representation(data)


class CommentChildrenSerializer(serializers.Serializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):

    children = CommentChildrenSerializer(many=True)

    class Meta:
        model = Comment
        list_serializer_class = FilterCommentSerializer
        fields = ('author_name', 'content', 'creation_date', 'children')


class NewsPostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = NewsPost
        fields = '__all__'
