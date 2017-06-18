from django.conf.urls import url
from . import views

app_name = 'myadmin'
urlpatterns = [
	url(r'^blog/$', views.bloglist, name='bloglist'),
	url(r'^blog/(?P<blog_id>[0-9]+)(?P<method>[a-z]+)/$', views.delete_blog, name='delete_blog'),
	url(r'^blog/(?P<blog_id>[0-9]+)/change/$', views.change, name='change'),
	url(r'^blog/add/$', views.create_blog, name='create_blog'),
	url(r'^blog/save/$', views.save_blog, name='save_blog'),
	url(r'^blog/saveChange/(?P<blog_id>[0-9]+)/$', views.save_change, name='save_change'),
	url(r'^classification/add/$', views.create_classi_tag, name='create_classi_tag'),
	url(r'^classification/save/$', views.save_classi, name='save_classi'),
	url(r'^tag/add/$', views.create_classi_tag, name='create_classi_tag'),
	url(r'^tag/save/$', views.save_tag, name='save_tag'),
	
]