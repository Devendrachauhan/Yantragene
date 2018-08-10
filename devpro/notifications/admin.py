from django.contrib import admin
from .models import Notification

# Register your models here.

class AdminNotification(admin.ModelAdmin):
	list_display = ['nid', 'notify']
	list_editable = ['notify']
	
admin.site.register(Notification, AdminNotification)
