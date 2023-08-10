from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from wanderHands.models import Post, Favorite, Image
from .permissions import IsOwnerOrReadOnly
from .serializers import postSerializer, favoriteSerializer, imageSerializer, favbyuserSerializer, CreateFavoriteSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
# @parser_classes([MultiPartParser, FormParser])
def post_list(request):
    if request.method == 'GET':

        post = Post.objects.all()
        serializer = postSerializer(post, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = postSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def post_details(request, pk):
    permission_classes = (IsOwnerOrReadOnly,)
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        serializer = postSerializer(post)
        return Response(serializer.data)
    if request.method == 'PUT':
        post = Post.objects.get(pk=pk)
        serializer = postSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def favorite_list(request):
    if request.method == 'GET':
        favorites = Favorite.objects.all()
        serializer = favoriteSerializer(favorites, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CreateFavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def favorite_details(request, pk):
    permission_classes = (IsOwnerOrReadOnly,)
    if request.method == 'GET':
        favorite = Favorite.objects.get(pk=pk)
        serializer = favoriteSerializer(favorite)
        return Response(serializer.data)
    if request.method == 'DELETE':
        favorite = Favorite.objects.get(pk=pk)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def favorite_by_user(request, pk):
    if request.method == 'GET':
        favorites = Favorite.objects.filter(user=pk)
        serializer = favbyuserSerializer(favorites, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def posts_by_user(request, pk):
    if request.method == 'GET':
        post = Post.objects.filter(author=pk)
        serializer = postSerializer(post, many=True)
        return Response(serializer.data)
