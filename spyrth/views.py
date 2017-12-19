# -*- coding: utf-8 -*-
from django.views import generic
from .models import *
from django.shortcuts import render
from .forms import *

class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

def about(request):
	template_name= "about.html"
	form_class = ContribForm
	if request.POST:
		form = form_class(request.POST)
		if form.is_valid():
			form.save()
			message = "Votre message a été envoyé. Merci"
	else:
		form=form_class()
		message =''
	return render(request, template_name, {'form':form})

def getprograms(request):
	template_name = "programs.html"
	allp = Programs.objects.all()
	form_class= SubscriptionForm
	if request.POST:
		form = form_class(request.POST)
		if form.is_valid():
			#subscribed=form.cleaned_data["email"]
			form.save()
			message = "Votre adresse mail a été bien enregistré, nous vous reviendrons très vite"
	else:
		form=form_class()	
		message = ''	
	return render(request, template_name, {'program': allp, 'form':form, 'message':message})

class ProgramsPage(generic.TemplateView):
	"""docstring for ServicesPage"""
	template_name = "programs.html"
	#def __init__(self, arg):
	#	super(ServicesPage, self).__init__()
	#	self.arg = arg

class ApplyPage(generic.TemplateView):
	"""docstring for ApplyPage"""
	template_name = "apply.html"
	#def __init__(self, arg):
	#	super(ApplyPage, self).__init__()
	#	self.arg = arg

class BlogPage(generic.TemplateView):
		"""docstring for BlogPage"""
		template_name ="blog.html"
		#def __init__(self, arg):
	#	super(BlogPage, self).__init__()
	#	self.arg = arg

class NotFoundPage(generic.TemplateView):
	template_name="404.html"