from django.http import HttpResponse


def index(request):
	return HttpResponse("Welcome to Poll.me!")

def detail(request, poll_id):
	return HttpResponse("Showing details of poll: %s" % poll_id)

def results(request, poll_id):
	return HttpResponse("Showing results of poll: %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("Vote on poll: %s" % poll_id)