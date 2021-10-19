from rest_framework import serializers
from .models import NewsPost, Comment, Upvote


class NewsPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = "__all__"


class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        exclude = ("id", "amount_of_upvotes", "creation_date")


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = (
            "id",
            "creation_date",
        )


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


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
        fields = "__all__"


class NewsPostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = NewsPost
        fields = "__all__"


class CreateVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ("news_post", "vote")
