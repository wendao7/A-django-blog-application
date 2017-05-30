# -*- coding:UTF-8 -*-
from django import forms

class ClassificationsForm(forms.Form):
	ctitle = forms.CharField(label="分类内容",widget=forms.TextInput())

class TagsForm(forms.Form):
	ttitle = forms.CharField(label="标签内容",widget=forms.TextInput())

class BlogForm(forms.Form):
	btitle = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'style':'display:none'}))
	btags = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none'}))
	bclassifications = forms.CharField(widget=forms.TextInput(attrs={'style':'display:none'}))
	bcontent = forms.CharField(widget=forms.Textarea(attrs={'style':'display:none'}))