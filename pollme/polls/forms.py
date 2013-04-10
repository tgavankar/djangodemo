from django import forms

from polls.models import Poll, Choice

class PollForm(forms.Form):
	# here we use a dummy `queryset` because ModelMultipleChoiceField
    # requires some queryset
	choices = forms.ModelMultipleChoiceField(queryset=Choice.objects.none(), widget=forms.CheckboxSelectMultiple())

	def __init__(self, poll_id, *args, **kwargs):
		super(PollForm, self).__init__(*args, **kwargs)
		self.fields['choices'].queryset = Poll.objects.get(pk=poll_id).choice_set.all()