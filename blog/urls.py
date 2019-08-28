from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("feed", views.feed, name="feed"),
    path("blogpost/<int:pId>", views.blogpost, name = "blogpost")
]