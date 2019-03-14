from django import forms
from .models import WebSite

class CreateWebsite(forms.ModelForm):
  
  class Meta:
    model = WebSite
    fields = ('name','url','description','designer','designer_url', 'twitter',
              'image1','image2','image3')

    widgets = {
	  'name': forms.TextInput(attrs={
	  	  'type' : 'text',
	  	  'placeholder' : 'Nombre del sitio'
	  	}),
	  'url': forms.TextInput(attrs={
	  	  'type' : 'url',
	  	  'placeholder' : 'url'

	  	}),
	  'description': forms.TextInput(attrs={
	  	  'type' : 'text',
	  	  'placeholder' : 'Descripcion'

	  	}),
	  'designer': forms.TextInput(attrs={
	  	  'type' : 'text',
	  	  'placeholder' : 'Diseñado por'

	  	}),
	  'designer_url': forms.TextInput(attrs={
	  	  'type' : 'text',
	  	  'placeholder' : 'Diseñador url'

	  	}),
	  'twitter': forms.TextInput(attrs={
	  	  'type' : 'text',
	  	  'placeholder' : 'Twitter'

	  	}),

    }