# encoding: utf-8 

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
import datetime
from django.utils.translation import ugettext_lazy as _



class Programs(models.Model):
	title = models.CharField(max_length = 30)
	shortDesc = models.TextField()
	picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
	url = models.URLField(blank=True)
	"""docstring for programs"""
	''' def __init__(self, arg):
		super(programs, self).__init__()
		self.arg = arg '''
	def __unicode__(self):
		return self.title

ContribType = ((0, ("Vous êtes:")),
				(1, ('Formateur')),
				(2, ('Sponsor')),
				(3, ('Partenaire Technique')),
				(4, ('Partenaire Financier')),
				(5, ('Mentor')),
				(6, ('Candidat à Naweza')),
				(7, ('Autres')),)
class ContactContrib(models.Model):
	Nom = models.CharField(max_length=200)
	Email = models.CharField(max_length=100, blank=True)
	Phone = models.CharField(max_length=50, blank=True)
	Pays =models.CharField(max_length=50, blank=True)
	Contrib = models.IntegerField(choices=ContribType, default=0)
	Autres = models.TextField(blank=True)


''' for newsletter '''
class SubscriptionBase(models.Model):
	subscribed = models.BooleanField(_('subscribed'), default=True)
	email = models.EmailField(_('email'), unique=True)
	created_on = models.DateField(_("created on"), blank=True)
	updated_on = models.DateField(_("updated on"), blank=True)

	class Meta:
		abstract =True
	@classmethod
	def is_subscribed(cls, email):
		try:
			return cls.objects.get(email=email).subscribed
		except cls.DoesNotExist, e:
			return False

	def __unicode__(self):
		return u'%s' %(self.email)
	def save(self, *args, **kwargs):
		self.updated_on = datetime.date.today()
		if not self.created_on:
			self.created_on = datetime.date.today()
		super(SubscriptionBase, self).save(*args, **kwargs)

class Subscription(SubscriptionBase):
	def save(self, *args, **kwargs):
		super(Subscription, self).save()

