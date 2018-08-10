from django.contrib import admin

# Register your models here.
from .models import Gallery

class AdminGallery(admin.ModelAdmin):
	list_display=['iname','image']

admin.site.register(Gallery,AdminGallery)