from rest_framework import serializers
from .models import Post, Favorite, Image
from rest_framework.serializers import CurrentUserDefault


class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'post', 'image']


class postSerializer(serializers.ModelSerializer):
    images = imageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'location', 'start_date',
                  'end_date', 'description', 'phone', 'email', 'author_id', 'author_name', 'images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            newpost_image = Image.objects.create(post=post, image=image)
        return post

# favbyuserse   rializer to show all favorites by user in post detail


class favbyuserSerializer(serializers.ModelSerializer):
    # Assuming you have a serializer named postSerializer for Post model
    post = postSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'post')


class favoriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = postSerializer()

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'post']


# CreatefavoriteSerializer


class CreatefavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post = postSerializer()

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'post']


class CreateFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('user', 'post')
