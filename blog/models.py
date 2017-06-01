# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
	title = models.CharField(max_length=20,unique=True)

	def __str__(self):
		return self.title

class Classification(models.Model):
	title = models.CharField(max_length=20,unique=True)

	def __str__(self):
		return self.title
		
class Blog(models.Model):
	title = models.CharField(max_length=50)
	views = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag,related_name='tag_arts')
	classifications = models.ForeignKey(Classification)
	content = models.TextField() 
	publish = models.BooleanField(default=False)
	pub_date = models.DateTimeField(auto_now_add=True)
	change_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'blog_id': self.pk})

	class Meta:
		ordering = ['-pub_date']

class Guest(models.Model):
    avatar = models.CharField(max_length=256, default='/blog/images/avatar.png')
    nick = models.CharField(max_length=128,default="路人甲")

    def __str__(self):
        return '{0}'.format(self.nick)

class Comment(models.Model):
	content = models.TextField()
	author = models.ForeignKey(Guest, related_name='user_comments', null=True, blank=True, on_delete=models.SET_NULL)
	belong = models.ForeignKey(Blog,related_name='blog_comments')
	comment_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{0}-{1}'.format(self.author, self.comment_time.strftime("%Y-%m-%d %H:%M:%S"))

class CommentReply(models.Model):
    content = models.TextField()
    comment = models.ForeignKey(Comment, related_name='comment_replies')
    author = models.ForeignKey(Guest, related_name='user_comment_replies', null=True, blank=True, on_delete=models.SET_NULL)
    to = models.ForeignKey(Guest, related_name='user_replied', null=True, blank=True, on_delete=models.SET_NULL)
    reply_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}->{1}'.format(self.author, self.to)











