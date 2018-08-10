from django.shortcuts import render
from event.models import Event, Participant

def about_view(request):
	
	context = {

		'events':Event.objects.all().count(),
		'teams_paricipated':Participant.objects.all().count(),
		'prize_money':'5 00 000'
		
	}

	
	return render(request ,'Aboutus/about.html', context)
