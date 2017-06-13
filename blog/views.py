# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, get_list_or_404, render,HttpResponse,redirect,render_to_response
from django.core.paginator import Paginator
from helper.paginator import getPages, getAbsPages
from django.core.urlresolvers import reverse 

from .models import Blog,Tag,Comment,Guest,CommentReply,Classification
from users.models import User
from .forms import CommentForm, CommentReplyForm
import markdown

def isUserLoginedDetail(request):
	context = {}
	if request.user.is_authenticated():
		context['commentSub'] = CommentForm()
		context['commentReplySub'] = CommentReplyForm()
		context['message'] = ''
	else:
		context['commentSub'] = ''
		context['commentReplySub'] = ''
		context['message'] = '登陆后评论'
	context['user'] = request.user
	return context

def index(request):
	blog_lists = Blog.objects.all()
	pages, blogs = getPages(request, blog_lists)

	context = {}
	context['user'] = request.user
	context['blogs'] = blogs
	context['pages'] = pages
	context['disable'] = 'disable'

	return render(request,'blog/index.html', context)

def archives(request, year, month):
	blog_list = Blog.objects.filter(pub_date__year = year).filter(pub_date__month = month)
	pages, blogs = getPages(request, blog_list)

	context = {}
	context['user'] = request.user
	context['blogs'] = blogs
	context['pages'] = pages
	context['disable'] = 'disable'

	return render(request,'blog/index.html', context)

def category(request, pk):
	cate = get_object_or_404(Classification, pk=pk)
	blog_list = Blog.objects.filter(classifications=cate)

	pages, blogs = getPages(request, blog_list)

	context = {}
	context['user'] = request.user
	context['blogs'] = blogs
	context['pages'] = pages
	context['disable'] = 'disable'
	return render(request,'blog/index.html', context)


def detail(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	blog.views += 1
	blog.save()
	tags = blog.tags.all()

	comments = blog.blog_comments.all()

	context = isUserLoginedDetail(request)
	context['blog'] = blog
	context['tags'] = tags
	context['comments'] = comments

	return render(request, 'blog/detail.html', context)

def trick(request):
	context = {}
	context['user'] = request.user
	return render(request, 'blog/trick.html',context)

def about(request):
	context = {}
	context['user'] = request.user
	return render(request, 'blog/about.html',context)

def abstract(request):
	blog_lists = Blog.objects.all()
	pages, blogs = getAbsPages(request, blog_lists)

	context = {}
	context['user'] = request.user
	context['blogs'] = blogs
	context['pages'] = pages
	context['disable'] = 'disable'
	return render(request, 'blog/abstract.html', context)

def comment(request,blog_id):
	if request.method == 'POST':
		belong = get_object_or_404(Blog,pk=blog_id)
		form = CommentForm(request.POST)

		if request.user.is_authenticated():
			if form.is_valid():
				content = form.cleaned_data['content']
		        comment = Comment()
		       
		        user = User.objects.get(username=request.user.username)

		        comment.content = content
		        comment.author = user
		        comment.belong = belong

		        comment.save()
		return redirect(belong)



def commentReply(request, blog_id):
	if request.method == 'POST':
		form = CommentReplyForm(request.POST)
		if form.is_valid():
			contentc = form.cleaned_data['contentc']
			cid = form.cleaned_data['cid']
			toid = form.cleaned_data['toid']
	        comment = get_object_or_404(Comment,pk=cid)

	        user = User.objects.get(username=request.user.username)
	        toAuthor = get_object_or_404(User,pk=toid)

	        commentRe = CommentReply()
	        commentRe.content = contentc
	        commentRe.comment = comment
	        commentRe.author = user
	        commentRe.to = toAuthor

	        commentRe.save()

	        blog = get_object_or_404(Blog,pk=blog_id)
		return redirect(blog)








