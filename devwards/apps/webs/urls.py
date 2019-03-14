from django.conf.urls import url
from . import views
from .views import SendWebsiteView, WebsiteDetailView, WebSiteVoteView, VoteAjax

app_name="webs"

urlpatterns = [
  url(r'^vote/$', VoteAjax.as_view(), name='vote'),
  url(r'^sitios/enviar/$', SendWebsiteView.as_view(), name='send'),
  url(r'^sitios/(?P<slug>[-\w]+)/$', WebsiteDetailView.as_view(), name='website_detail'),
  url(r'^sitios/(?P<slug>[-\w]+)/votar/$', WebSiteVoteView.as_view(), name='website_vote'),
]
