from django.urls import path
from .views import post_list,post_details, favorite_list, favorite_details, favorite_by_user, posts_by_user

urlpatterns = [
    path("post/", post_list, name="post_list"),
    path("post/<int:pk>/", post_details, name="post_detail"),
    path("favorites/", favorite_list, name="favorite_list"),
    path("favorites/<int:pk>/", favorite_details, name="favorite_detail"),
    #favs by user
    path("favorites/user/<int:pk>/", favorite_by_user, name="favorite_by_user"),
    #posts by user
    path("post/user/<int:pk>/", posts_by_user, name="posts_by_user"),

]
