from django.shortcuts import render, redirect
from backend.forms import RegistrationForm, EditUserForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm  
from django.contrib.auth.models import User  
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required  
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import(
    ListView, DetailView, CreateView, UpdateView, DeleteView)    
from django.views import View
from . import forms



# Create your views here.

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			email = form.cleaned_data.get('email')
			user = authenticate(request, username=username, password=raw_password, email=email)
			login(request, user)
			return redirect('blog:list')
	else:
		form = RegistrationForm()
	return render(request, 'backend/register.html', {'form': form})			

	def post(self, request):
		form = forms.RegistrationForm(request.POST)		 
		if form.is_valid():
			form.deploy()
		return render(request, self.template_name, {'form':form})



@login_required 
def change_password(request):
	if request.method == 'POST':
		pass_form = PasswordChangeForm(data=request.POST, user=request.user)
		if pass_form.is_valid():
			pass_form.save()
			update_session_auth_hash(request, pass_form.user)
			messages.success(request, 'Password changed successfully.')
			return redirect('backend:login')
	else:
		pass_form = PasswordChangeForm(user=request.user) 

	return render(request, 'backend/change_password.html', {'pass_key':pass_form})
					
def reset_password(request): 
	return render(request, 'backend/reset_password.html')

@login_required
def edit_form(request):
	if request.method == 'POST':
		edit_form = EditUserForm(request.POST, instance=request.user)
		if edit_form.is_valid():
			edit_form.save()
			messages.success(request, 'User edited successfully.')
			return redirect('backend:view_profile')
	else:
		edit_form = EditUserForm(instance=request.user)
	return render(request, 'backend/edit_form.html', {'edit_key':edit_form})


		


