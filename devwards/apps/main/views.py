from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from apps.webs.models import WebSite

# Create your views here.

class HomeView(TemplateView):
	template_name= 'home.html'

	def get_context_data(self, **kargs):
		context = super(HomeView, self).get_context_data(**kargs)
		context['last_website'] = WebSite.objects.last()
		context['websites'] = WebSite.objects.exclude(id = context['last_website'].id)

		return context