from rest_framework import serializers
from ..models.blog import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'author', 'content', 'updated_at', 'created_at')