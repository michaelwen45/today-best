from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.getPostList, name="post_list"),
]