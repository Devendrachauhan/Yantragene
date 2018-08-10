from django.db import models

# Create your models here.
class Gallery(models.Model):
	iname=models.CharField(max_length=20)
	image=models.ImageField(upload_to='images/gallery',blank=True)

	def __str__(self):
		return self.iname
