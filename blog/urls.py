from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<blog_id>[0-9]+)/comment$', views.comment, name='comment'),
	url(r'^(?P<blog_id>[0-9]+)/commentReply$', views.commentReply, name='commentReply'),
	url(r'^abstract$', views.abstract, name='abstract'),
	url(r'^trick$', views.trick, name='trick'),
	url(r'^about$', views.about, name='about'),
]