from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cupcake(models.Model):
	name = models.CharField(max_length=200)
	price = models.CharField(max_length=20)
	rating = models.FloatField()
	image = models.ImageField(upload_to="post_images")
	writer = models.ForeignKey(User)
	createdAt = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
			return self.name
		
class Post(models.Model):
	name = models.CharField(max_length=20)
	content = models.CharField(max_length=200)
	best = models.IntegerField()
	writer = models.ForeignKey(User)
	createdAt = models.DateTimeField(default=timezone.now)
	def __str__(self):
			return self.name
	
	