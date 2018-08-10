from django.db import models
from accounts.models import Profile


class Branch(models.Model):
	bid=models.IntegerField()
	bran=models.CharField(max_length=200)
	bimage=models.ImageField(upload_to='images', null=True)
	def __str__(self):
		return self.bran

class Event(models.Model):
	eid = models.IntegerField()
	branch=models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
	eve=models.CharField(max_length=200)
	def __str__(self):
		return self.eve

class Coordinator(models.Model):
	event=models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
	coord=models.CharField(max_length=200)
	cimage=models.ImageField(upload_to='images',blank=True)
	mob=models.CharField(max_length=20, blank=True)
	email=models.EmailField(blank=True)

	def __str__(self):
		return self.coord



class Participant(models.Model):
	events = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	team_name = models.CharField(max_length=30, blank=True, null=True)
	events_name = models.CharField(max_length=30, blank=True, null=True)
	pname2 = models.CharField(max_length=50, blank=True, null=True)
	pname3 = models.CharField(max_length=50, blank=True, null=True)
	pname4 = models.CharField(max_length=50, blank=True, null=True)
	pname5 = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.team_name

