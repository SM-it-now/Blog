from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'post', 'author', 'content', 'create_at', 'modify_at'
        )
        read_only_fields = ('post',)


class PostSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

