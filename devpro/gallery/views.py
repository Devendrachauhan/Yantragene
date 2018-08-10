from django.shortcuts import render
from .models import Gallery
# Create your views here.

def gallery_view(request):
	images=Gallery.objects.all()

	return render(request, 'Gallery/gallery.html', {'images':images})