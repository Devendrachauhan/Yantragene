from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Branch, Coordinator, Event, Participant


def branch(request):
	branch_all=Branch.objects.all()
	evt=Event.objects.all()
	g=dict()
	for i in branch_all:
		e=evt.filter(branch=i)
		g[i]=e


	context={'outer_event':g,
				'branch_all':branch_all}
 
	return render(request, 'Events/event.html',context)


def event_detail(request, id=None):
	event=get_object_or_404(Event, id=id)
	coordinate=Coordinator.objects.filter(event=event)

	page = event.eve.lower()
	page = 'Events/'+page+'.html'

	
	context={ 
				'event_title' : event.eve.upper(),
				'event':event,
				'cod':coordinate
	}
				
	return render(request,page, context)

def register_view(request):
	team_name=request.GET['team_name']
	pname2=request.GET['pname2']
	pname3=request.GET['pname3']
	pname4=request.GET['pname4']
	pname5=request.GET['pname5']
	event_id = request.GET['event_id']
	profile_id = request.GET['profile_id']
	events_name = request.GET['events_name']

	t = Participant.objects.filter(team_name=team_name)
	if len(t):
		return render(request, 'Events/event.html', {'msg':'Team name already existed'})

	t = Participant.objects.filter(events_name=events_name, profile=profile_id)
	if len(t):
		return render(request, 'Events/event.html', {'msg':'You have already participated in this event'})

	p = Participant(

		team_name=team_name,
		events_name=events_name, 
		pname2=pname2, 
		pname3=pname3,
		pname4=pname4,
		pname5=pname5,
		events_id=event_id,
		profile_id=profile_id,

		)

	p.save()

	return HttpResponseRedirect(reverse('event:event'))