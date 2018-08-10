from django.db import models

# Create your models here.
class Notification(models.Model):
	nid=models.IntegerField()
	notify=models.TextField(max_length=200)

	def __str__(self):
		return self.notify