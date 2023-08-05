from rest_framework import serializers
from .models import Post, Favorite


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'location', 'start_date',
                  'end_date', 'description', 'images']


class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'post']
