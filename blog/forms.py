# -*- coding:UTF-8 -*-

from django import forms

class CommentForm(forms.Form):
	content = forms.CharField(label='评论内容')

class CommentReplyForm(forms.Form):
	contentc = forms.CharField(label='回复内容')
	cid = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none'}))
	toid = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none'})) 