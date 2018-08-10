from django.contrib import admin
from .models import Branch, Event, Coordinator, Participant


class AdminBranch(admin.ModelAdmin):
	list_display = ['bran']
	list_editable = ['bran']

class AdminEvent(admin.ModelAdmin):
	list_display = ['eve']
	list_editable = ['eve']

class AdminCoordinator(admin.ModelAdmin):
	list_display = ['coord', 'email', 'mob']
	list_editable = ['coord', 'email', 'mob']


class AdminParticipant(admin.ModelAdmin):
	list_display = ['team_name', 'events_name', 'pname2', 'pname3', 'pname4', 'pname5']

admin.site.register(Branch, AdminBranch)
admin.site.register(Event, AdminEvent)
admin.site.register(Coordinator, AdminCoordinator)
admin.site.register(Participant, AdminParticipant)