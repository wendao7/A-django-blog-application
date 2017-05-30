# -*- coding:UTF-8 -*-

from django import forms

class CommentForm(forms.Form):
	cname = forms.CharField(label="江湖过客",widget=forms.Textarea(attrs={
		'placeholder':'随心评论,何必注册.敝人名讳:',
		}))
	content = forms.CharField(label='评论内容')

class CommentReplyForm(forms.Form):
	crname = forms.CharField(label="江湖过客",widget=forms.Textarea(attrs={
		'placeholder':'随心评论,何必注册.江湖人称:',
		}))
	contentc = forms.CharField(label='回复内容')
	cid = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none'}))
	toid = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none'})) 