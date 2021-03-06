from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


def home(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    context = {
        'title': post,
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/detail.html', context)
