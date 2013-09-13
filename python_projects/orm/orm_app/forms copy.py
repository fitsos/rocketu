from django import forms
from orm_app.models import Poll
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# class  (UserForm):

# 	user = authenticate(username= username, password= password)
# 	if user is not None:
# 		# do something for an authed user, maybe a redirect?

class UserForm(forms.ModelForm):
  class Meta(object):
      model = User
      fields = ["username", "email", "password"]
      widgets = {
	      "password":forms.PasswordInput
      }

class SignupForm(UserForm):
	confirm_password = forms.CharField(
		widget = forms.PasswordInput
	)

def clean(self):
	password = self.cleaned_data.get('password')
	password_conf = self.cleaned_data.get('confirm_password')
	if password is not None and password != password_conf:
		raise forms.ValidationError (
			"Password confirmation does not match password"
		)
	return self.cleaned_data

class PollAnswerForm(forms.Form):
    poll = forms.ModelChoiceField(queryset=Poll.objects.all())
    answer = forms.CharField()

class PollForm(forms.ModelForm):

    class Meta(object):
        model = Poll
        fields = ['question']

class PollQuestionForm(forms.Form):
    question = forms.CharField()

class SignupForm(UserForm):
    confirm_password = forms.CharField(
    	widget = forms.PasswordInput
    )

