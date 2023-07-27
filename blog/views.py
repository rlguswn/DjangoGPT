from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer


class PostIndex(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostWrite(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PostUpdate(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class PostDelete(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({'message': 'Post deleted'}, status=204)


class CommentWrite(APIView):
    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CommentDelete(APIView):
    def get(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return Response({'message': 'Comment deleted'}, status=204)
