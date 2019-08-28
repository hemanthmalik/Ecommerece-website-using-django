from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.


def index(request):
    shit = BlogPost.objects.all()
    return render(request, "blog/index.html", {"shit": shit})


def feed(request):
    return HttpResponse("this is the feed page")


def blogpost(request, pId):
    blog = BlogPost.objects.get(post_id=pId)
    return render(request, "blog/blogpost.html", {"blog": blog})