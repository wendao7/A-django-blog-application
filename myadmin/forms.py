# -*- coding:UTF-8 -*-
from django import forms

class ClassificationsForm(forms.Form):
	ctitle = forms.CharField(label="分类内容",widget=forms.TextInput())

class TagsForm(forms.Form):
	ttitle = forms.CharField(label="标签内容",widget=forms.TextInput())