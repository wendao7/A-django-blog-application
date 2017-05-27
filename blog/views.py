# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, get_list_or_404, render,HttpResponse,redirect
from django.core.paginator import Paginator
from helper.paginator import getPages, getAbsPages
from django.core.urlresolvers import reverse 

from .models import Blog,Tag,Comment,Guest,CommentReply

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

	context = {
		'blog':blog,
		'tags':tags,
		'comments':comments,
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


# Create your views here.

def comment(request,blog_id):
    if request.POST:
        content = request.POST['comment_content']

        comment = Comment()
        belong = get_object_or_404(Blog,pk=blog_id)
        author = Guest()
        author.save()

        comment.content = content
        comment.author = author
        comment.belong = belong

        comment.save()

        bid = blog_id

    return redirect(reverse('blog:detail', args=(bid,)))


def commentReply(request, blog_id):
    if request.POST:
        content = request.POST['commentReply_content']
        cid = request.POST['comment_id']
        to_id = request.POST['toAuthor_id']

        commentRe = CommentReply()
        commentRe.content = content
        comment = get_object_or_404(Comment,pk=cid)
        commentRe.comment = comment
        
        author = Guest()
        author.save()

        commentRe.author = author 
        toAuthor = get_object_or_404(Guest,pk=to_id)

        commentRe.to = toAuthor

        commentRe.save()

        bid = blog_id

    return redirect(reverse('blog:detail', args=(bid,)))








