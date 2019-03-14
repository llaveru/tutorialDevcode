from django.contrib import admin

# Register your models here.
from .models import WebSite, Vote
#registra WebSite el modelo para verlo en la pagina de admin

@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
  pass

@admin.register(Vote)
class WebSiteAdmin(admin.ModelAdmin):
  pass
