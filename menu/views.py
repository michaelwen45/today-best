from django.shortcuts import render
from . import models
from .models import Cupcake

def cupcake_list(request):
	cakes = Cupcake.objects.all().order_by('-createdAt')
	context = {"cakes": cakes}
	return render(request,"menu/list.html",context)

# Create your views here.
