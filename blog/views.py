from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .templates import *
from .models import *


# Create your views here.


class MainPageView(View):
    def get(self, request):
        data = Post.objects.all()
        return render(request, 'blog/index.html', {'posts': data})
