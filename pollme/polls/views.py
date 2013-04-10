from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from polls.forms import PollForm
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("Showing results of poll: %s" % poll_id)

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST': # If the form has been submitted...
        form = PollForm(poll_id, request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            choices = form.cleaned_data['choices']
            choices.update(votes=F('votes') + 1)
            return HttpResponse('Saved') # Redirect after POST
    else:
        form = PollForm(poll_id) # An unbound form

    return render(request, 'polls/vote.html', {
        'form': form,
        'poll': poll,
    })