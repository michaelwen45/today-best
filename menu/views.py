from django.shortcuts import render
from . import models
from .models import Cupcake
from .models import Post


def cupcake_list(request):
	cakes = Cupcake.objects.all().order_by('-createdAt')
	context = {"cakes": cakes}
	return render(request,"menu/list.html",context)

def getPostList(request):
	posts = Post.objects.all().order_by('-createdAt')
	context = {"posts": posts}
	return render(request,"menu/list.html",context)

# Create your views here.
