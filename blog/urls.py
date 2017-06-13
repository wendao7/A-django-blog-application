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
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]