from django import template
from ..models import Blog, Classification

register = template.Library()

@register.simple_tag
def get_recent_blogs(num=5):
	return Blog.objects.all().order_by('-pub_date')[:num]

@register.simple_tag
def get_hotest_blogs(num=5):
	return Blog.objects.order_by('-views')[:num]

@register.simple_tag
def archives():
	return Blog.objects.dates('pub_date','month', order='DESC')

@register.simple_tag
def get_classifications():
	return Classification.objects.all()