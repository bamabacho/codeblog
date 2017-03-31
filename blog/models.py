from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 250)
	text = models.TextField()
	image = models.FileField(upload_to='documents', default=False)
	created_date = models.DateTimeField( default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		se;lf.save()

	def __str__(self):
		return self.title
		