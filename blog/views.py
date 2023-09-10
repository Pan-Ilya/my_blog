from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .templates import *
from .models import *


# Create your views here.


class MainPage(View):
    def get(self, request):
        posts = Post.objects.all()
        pagintor = Paginator(posts, 3)

        page_number = request.GET.get('page')
        page_obj = pagintor.get_page(page_number)

        return render(request, 'blog/index.html', {'page_obj': page_obj})


class ShowPost(View):
    def get(self, request, url_name):
        post = get_object_or_404(Post, url=url_name)

        return render(request, 'blog/post.html', {'post': post})
