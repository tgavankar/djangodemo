from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	return HttpResponse("Showing details of poll: %s" % poll_id)

def results(request, poll_id):
	return HttpResponse("Showing results of poll: %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("Vote on poll: %s" % poll_id)