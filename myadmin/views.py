# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect,reverse, HttpResponse
from blog.models import Classification,Tag,Blog

from .forms import ClassificationsForm, TagsForm

# Create your views here.
def create_blog(request):
	classifications = Classification.objects.all()
	tags = Tag.objects.all()
	context = {
		'classifications': classifications,
		'tags': tags,
	}
	return render(request, 'myadmin/blog_add.html', context)

def save_blog(request):
	if request.POST:
		title = request.POST['blog_title']
		cla_id = request.POST['group1']
		tags = request.POST['tags_id'].split("#")
		content = request.POST['newBlog_content']

		blog = Blog()
		blog.title = title
		blog.classifications = get_object_or_404(Classification,pk=cla_id)
		blog.save()
		blog.content = content

		for tag in tags:
			tag_ins = get_object_or_404(Tag,pk=tag)
			blog.tags.add(tag_ins)

		blog.save()

	return redirect(reverse('myadmin:bloglist', args=()))

def create_classi_tag(request):
	tags = Tag.objects.all();
	cls = Classification.objects.all();
	cForm = ClassificationsForm()
	tForm = TagsForm()
	context = {
		'tags':tags,
		'cls':cls,
		'cForm': cForm,
		'tForm': tForm,
	}
	return render(request, 'myadmin/classi_tag_add.html',context)

def save_classi(request):
	if request.method == 'POST':
		form = ClassificationsForm(request.POST)
		if form.is_valid():
			classis = form.cleaned_data['ctitle'].split(',')
			for classi in classis:
				cl_ins = Classification()
				cl_ins.title = classi
				cl_ins.save()
	return redirect(reverse('myadmin:create_classi_tag', args=()))

def save_tag(request):
	if request.method == 'POST':
		form = TagsForm(request.POST)
		if form.is_valid():
			tags = form.cleaned_data['ttitle'].split(',')
			for tag in tags:
				tag_ins = Tag()
				tag_ins.title = tag
				tag_ins.save()
	return redirect(reverse('myadmin:create_classi_tag', args=()))

def bloglist(request):
	blogs = Blog.objects.all()
	context = {
		'blogs':blogs,
	}
	return render(request, 'myadmin/bloglist.html', context)

def delete_blog(request,blog_id,method):
	if method == "d":
		blog = get_object_or_404(Blog,pk=blog_id)
		comments = blog.blog_comments.all()
		if comments:
			for comment in comments:
				creplys = comment.comment_replies.all()
				if creplys:
					for creply in creplys:
						creply.delete()
				comment.delete()
		blog.delete()
	else:
		blog = get_object_or_404(Blog,pk=blog_id)
		blog.publish = True
		blog.save()

	return redirect(reverse('myadmin:bloglist', args=()))


