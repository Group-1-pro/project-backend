from django.contrib import admin
from .models import Post, Favorite, Image
# Register your models here.
admin.site.register(Post)
admin.site.register(Favorite)
admin.site.register(Image)

