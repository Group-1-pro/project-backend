from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    author_name = models.CharField(max_length=40, default='username')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    phone = models.CharField(max_length=15 , default = '123-456-7890')
    email = models.EmailField(default = 'email@email.com')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='favorites')
    class Meta:
            unique_together = ['user', 'post']

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title
