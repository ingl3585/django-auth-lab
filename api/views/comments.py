from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from ..serializers.comment import CommentSerializer
from ..models.comment import Comment


class CommentsView(APIView):
    def post(self, request):
        # Add the user id as author
        request.data['author'] = request.user.id
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentView(APIView):
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        # Check the comment's author against the user making this request
        if request.user != comment.author:
            raise PermissionDenied('Unauthorized, you do not own this comment')
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        # Check the comment's author against the user making this request
        if request.user != comment.author:
            raise PermissionDenied('Unauthorized, you do not own this comment')
        # Ensure the author field is set to the current user's ID
        request.data['author'] = request.user.id
        updated_comment = CommentSerializer(comment, data=request.data, partial=True)
        if updated_comment.is_valid():
            updated_comment.save()
            return Response(updated_comment.data)
        return Response(updated_comment.errors, status=status.HTTP_400_BAD_REQUEST)
