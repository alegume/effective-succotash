from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    users = User.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'users': users})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

def author_perfil(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)

    return render(request, 'blog/author_perfil.html', {'author': author, 'posts': posts})
