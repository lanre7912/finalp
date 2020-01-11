from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from final_app import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	first_name = forms.CharField(max_length=100, required=False, help_text='Optional', widget=forms.TextInput(attrs={'placeholder': 'Enter first name '}))
	last_name = forms.CharField(max_length=100, required=False, help_text='Optional', widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
	email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.', widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
	
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

		def clean_email(self):
			email = self.cleaned_data["email"]
			try:
				user = User.objects.get(email=email)
				raise forms.ValidationError("This email address already exists.")
			except User.DoesNotExist:
				return email

		def save(self, commit=True):
			user = super(UserCreationForm, self).save(commit=False)
			user.set_password(self, cleaned_data["password1"])
			user.email = self.cleaned_data["email"]
			user.is_active = True
			if commit:
				user.save()
			return user			
				

			
		
	
		

class EditUserForm(UserChangeForm):
	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')



class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)
		
	
			