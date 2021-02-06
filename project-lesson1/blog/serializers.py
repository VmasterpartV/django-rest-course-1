from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']

class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Post
        exclude = []
        # depth = 1

class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    post = PostSerializer

    class Meta:
        model = Comment
        exclude = []
        # depth = 1

