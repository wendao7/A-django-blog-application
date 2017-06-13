# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	nickname = models.CharField(max_length=50, blank=True)
	avatar = models.CharField(max_length=256, default='/blog/images/avatar.png')

	class Meta(AbstractUser.Meta):
		pass
		
	def __str__(self):
		return '{0}'.format(self.username)
			