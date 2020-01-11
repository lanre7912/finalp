from django.conf import settings
from django.shortcuts import render, redirect
from backend.forms import ContactForm
from django.contrib.auth.models import User 
from django.core.mail import send_mail
from django.template.loader import get_template
from django.contrib import messages


# Create your views here.
def index(request): 
  return render(request, 'final_app/index.html') 
def about(request): 
  return render(request, 'final_app/about.html') 
def courses(request): 
  return render(request, 'final_app/courses.html') 
def course_details(request): 
  return render(request, 'final_app/course-details.html') 
def elements(request): 
  return render(request, 'final_app/elements.html')


def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['lanre7912@gmail.com']
			if cc_myself:
				recipients.append(email)

			send_mail(subject, message, email, recipients, fail_silently=True)
			messages.success(request, 'Message sent successfully.')
			form = ContactForm()	
	else:
		form = ContactForm()		
	return render(request, 'final_app/contact.html', {'form': form})