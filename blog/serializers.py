from rest_framework import serializers
from .models import Post, Comment


class CommentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        field = '__all__'


class PostSerializers(serializers.ModelSerializer):
    comment = CommentSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

