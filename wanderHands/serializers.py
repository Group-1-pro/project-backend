from rest_framework import serializers
from .models import Post, Favorite, Image


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'location', 'start_date',
                  'end_date', 'description', 'phone', 'email', 'author']


class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'post']

class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'post', 'image']
