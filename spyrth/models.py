from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings




class programs(models.Model):
	title = models.CharField(max_length = 30)
	shortDesc = models.TextField()
	picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
	url = models.URLField()
	"""docstring for programs"""
	def __init__(self, arg):
		super(programs, self).__init__()
		self.arg = arg
