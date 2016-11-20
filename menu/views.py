from django.shortcuts import render
from . import models
from .models import Cupcake
from .models import Post
from django.shortcuts import render, get_object_or_404


def getPostList(request):
	posts = Post.objects.all().order_by('-createdAt')
	context = {"posts": posts}
	return render(request,"menu/list.html",context)

def	post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	context = {"post": post}
	return render(request, "menu/detail.html", context)
