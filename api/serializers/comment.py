from rest_framework import serializers
from ..models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'blog', 'author', 'content', 'updated_at', 'created_at')
