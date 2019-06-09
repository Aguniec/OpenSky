from django.shortcuts import render
import datetime


posts = [
    {
        "author": "Brad Pitt",
        "title": "Post_1",
        "content": "First post content",
        "date_posted": datetime.datetime.now

    },
    {
        "author": "Forest Gump",
        "title": "Post_2",
        "content": "Second post content",
        "date_posted": datetime.datetime.now

    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "flight/home.html", context)


def about(request):
    return render(request, "flight/about.html", {"title": "- About"})


# Create your views here.
