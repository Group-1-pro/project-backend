from django.shortcuts import render
from wanderHands.models import Post, Favorite, Image
from .permissions import IsOwnerOrReadOnly
from .serializers import postSerializer, favoriteSerializer, imageSerializer,favbyuserSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.shortcuts import get_object_or_404
# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
from rest_framework.response import Response


@api_view(['GET', 'POST'])
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
def favorite_list(request):
    permission_classes = (IsOwnerOrReadOnly,)
    if request.method == 'GET':
        favorite = Favorite.objects.all()
        serializer = favoriteSerializer(favorite, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = favoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def favorite_details(request, pk):
    permission_classes = (IsOwnerOrReadOnly,)
    if request.method == 'GET':
        favorite = Favorite.objects.get(pk=pk)
        serializer = favoriteSerializer(favorite)
        return Response(serializer.data)
    if request.method == 'PUT':
        favorite = Favorite.objects.get(pk=pk)
        serializer = favoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        favorite = Favorite.objects.get(pk=pk)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def image_list(request):
    permission_classes = (IsOwnerOrReadOnly,)
    if request.method == 'GET':
        image = Image.objects.all()
        serializer = imageSerializer(image, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = imageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def image_details(request, pk):
    permission_classes = (IsOwnerOrReadOnly,)
    if request.method == 'GET':
        image = Image.objects.get(pk=pk)
        serializer = imageSerializer(image)
        return Response(serializer.data)
    if request.method == 'PUT':
        image = Image.objects.get(pk=pk)
        serializer = imageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        image = Image.objects.get(pk=pk)
        image.delete()
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
