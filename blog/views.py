from django.shortcuts import render
from blog.models import Post


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )

    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_post(request, slug):
    post = Post.objects.get(slug=slug)

    context = {  # access in HTML template
        "post": post
    }
    return render(request, "blog_post.html", context)
