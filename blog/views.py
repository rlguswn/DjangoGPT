from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer


class PostIndex(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        # return Response(serializer.data)
        return render(request, 'blog/post_list.html', {'posts': serializer.data})


class PostDetail(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post_serializer = PostSerializer(post)
        # return Response(serializer.data)
        return render(request, 'blog/post_detail.html', {'post': post_serializer.data})


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


class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)


class CommentWrite(APIView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post, writer=request.user)
            # return Response(serializer.data, status=201)
            return redirect('blog:cm-list')
        return Response(serializer.errors, status=400)


class CommentDelete(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({'message': 'Comment deleted'}, status=204)
