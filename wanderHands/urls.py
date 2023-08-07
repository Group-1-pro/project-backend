from django.urls import path
from .views import post_list,post_details,image_list,image_details, favorite_list, favorite_details

urlpatterns = [
    path("post", post_list, name="post_list"),
    path("post/<int:pk>/", post_details, name="post_detail"),
    path("favorites/", favorite_list, name="favorite_list"),
    path("favorites/<int:pk>/", favorite_details, name="favorite_detail"),
    path("images/", image_list, name="image_list"),
    path("images/<int:pk>/", image_details, name="image_detail"),
]
