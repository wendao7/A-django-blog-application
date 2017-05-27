# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog,Tag,Classification,Guest,Comment,CommentReply

class BlogAdmin(admin.ModelAdmin):
	list_display = (
		"title",
		"views",
		"pub_date",
		"change_date",
	)

	#search_fields = ['blog_title']


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(Guest)
admin.site.register(Comment)
admin.site.register(CommentReply)