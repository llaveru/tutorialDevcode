# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, FormView, View #vista generica
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.urls  import  reverse_lazy, reverse
from django.contrib.auth import login, authenticate, logout

class LogoutView(View):
   def get(self, request, *args, **kwargs):
     logout(request)
     return redirect(reverse('main:home'))


class RegisterView(FormView):
   template_name='register.html'
   form_class = RegisterForm
   success_url=('http://localhost:8000/')

   def form_valid(self, form):
     user = form.save()
     user.set_password(form.cleaned_data['password'])
     user.save()
     return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
   template_name ='login.html'
   form_class=LoginForm
   success_url=('http://localhost:8000/')
# succes_url = reverse_lazy('users:login') no funcionaba
# Create your views here.

def form_valid(self,form):
  print('is valid')

  user = authenticate(
          username = form.cleaned_data['username'],
          password = form.cleaned_data['password']
	)
      
  login(self.request,user)
  return super(LoginView,self).form_valid(form)



