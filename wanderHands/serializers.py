from rest_framework import serializers
from .models import Post, Favorite, Image


class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'post']



class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'post', 'image']


class postSerializer(serializers.ModelSerializer):
    images = imageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'location', 'start_date',
                  'end_date', 'description', 'phone', 'email', 'author', 'images', 'uploaded_images']
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            newpost_image = Image.objects.create(post=post, image=image)
        return post
