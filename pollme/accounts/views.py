from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    return HttpResponse("Account profiles")

def register(request):
    if request.method == 'POST': # If the form has been submitted...
        form = UserCreationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username, None, password) # email = None
            return HttpResponse('Saved') # Redirect after POST
    else:
        form = UserCreationForm() # An unbound form

    return render(request, 'accounts/register.html', {
        'form': form,
    })