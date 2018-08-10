from django.contrib import admin
from .models import Feedback


class AdminFeedback(admin.ModelAdmin):
	list_display = ['name', 'email', 'review']

admin.site.register(Feedback,AdminFeedback)