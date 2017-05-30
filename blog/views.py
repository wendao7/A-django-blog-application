# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, get_list_or_404, render,HttpResponse,redirect
from django.core.paginator import Paginator
from helper.paginator import getPages, getAbsPages
from django.core.urlresolvers import reverse 

from .models import Blog,Tag,Comment,Guest,CommentReply

from .forms import CommentForm, CommentReplyForm

def index(request):
	latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
	hotest_blog_list = Blog.objects.order_by('-views')[:5]
	blog_lists = Blog.objects.all()
	pages, blogs = getPages(request, blog_lists)

	context = {
		'latest_blog_list': latest_blog_list,
		'hotest_blog_list': hotest_blog_list,
		'blogs': blogs,
		'pages':pages,
		'disable':'disabled',
	}
	return render(request,'blog/index.html', context)

def detail(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	blog.views += 1
	blog.save()
	tags = blog.tags.all()

	#comments = get_list_or_404(Comment, belong=blog_id)
	comments = blog.blog_comments.all()

	commentSub = CommentForm()
	commentReplySub = CommentReplyForm()

	context = {
		'blog':blog,
		'tags':tags,
		'comments':comments,
		'commentSub':commentSub,
		'commentReplySub':commentReplySub,
	}
	return render(request, 'blog/detail.html', context)

def trick(request):
	return render(request, 'blog/trick.html')

def about(request):
	return render(request, 'blog/about.html')

def abstract(request):
	blog_lists = Blog.objects.all()
	pages, blogs = getAbsPages(request, blog_lists)
	context = {
		'pages': pages,
		'blogs': blogs,
		'disable': 'disabled',
	}
	return render(request, 'blog/abstract.html', context)

def comment(request,blog_id):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			name = form.cleaned_data['cname']
	        comment = Comment()
	        belong = get_object_or_404(Blog,pk=blog_id)
	        author = Guest(nick=name)
	        author.save()

	        comment.content = content
	        comment.author = author
	        comment.belong = belong

	        comment.save()
	        bid = blog_id
    	return redirect(reverse('blog:detail', args=(bid,)))

def commentReply(request, blog_id):
	if request.method == 'POST':
		form = CommentReplyForm(request.POST)
		if form.is_valid():
			contentc = form.cleaned_data['contentc']
			name = form.cleaned_data['crname']
			cid = form.cleaned_data['cid']
			toid = form.cleaned_data['toid']

			print cid
	        comment = get_object_or_404(Comment,pk=cid)
	        author = Guest(nick=name)
	        author.save()
	        toAuthor = get_object_or_404(Guest,pk=toid)

	        commentRe = CommentReply()
	        commentRe.content = contentc
	        commentRe.comment = comment
	        commentRe.author = author 
	        commentRe.to = toAuthor

	        commentRe.save()

	        bid = blog_id
		return redirect(reverse('blog:detail', args=(bid,)))








