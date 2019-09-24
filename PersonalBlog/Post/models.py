from django.db import models
import django

# Create your models here.

class Post(models.Model):
	"""
		Los Post
	"""
	title = models.CharField(max_length=200, null=False)
	paragraph = models.TextField(null=False)
	date = models.DateTimeField(default=django.utils.timezone.now, null=False)
	image = models.ImageField(upload_to='posts', null=True)

	def __str__(self):
		return str(self.id) + " " + self.title
