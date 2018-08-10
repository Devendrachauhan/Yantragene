from django.shortcuts import render
from .models import Notification

def note_view(request):
	return render(request, 'notification/notify.html', {'notes':Notification.objects.all()})
