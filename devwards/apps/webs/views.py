from django.shortcuts import render
from django.http import JsonResponse
from .forms import CreateWebsite
from django.views.generic import FormView, CreateView, DetailView, View
from django.urls import reverse, reverse_lazy
from .models import WebSite, Vote
# Create your views here.

class SendWebsiteView(CreateView):
   template_name = 'enviar-sitio.html'
   form_class = CreateWebsite
   success_url = reverse_lazy('webs:send')

class WebsiteDetailView(DetailView):
   template_name= 'detalle.html'
   model = WebSite
   context_object_name = 'website'

class WebSiteVoteView(DetailView):
   template_name= 'vote.html'
   model = WebSite
   context_object_name = 'website'

   def get_context_data(self, **kwargs):
      context = super(WebSiteVoteView, self).get_context_data(**kwargs)
      print (kwargs['object'])
      context['already_vote'] = Vote.objects.filter(
         user = self.request.user,
         website = kwargs['object']
      ).exists()
      print(context['already_vote'])
      return context

class VoteAjax(View):

   def get(self, request, *args, **kwargs):
     website = WebSite.objects.get(id = request.GET['websiteID'])
     Vote.objects.create(
        user = request.user,
        website = website,
        design = int(request.GET['valDesign']),
        usability = int(request.GET['valUsability']),
        creativity = int(request.GET['valCreativity']),
        content = int(request.GET['valContent'])
      )
     return JsonResponse({ 'success': True })
