from django.conf.urls import url
from .views import RegisterView,LoginView,LogoutView


app_name='users'

urlpatterns = [
   url(r'^registrar/$', RegisterView.as_view(),name='register'),
   url(r'^ingresar/$', LoginView.as_view(),name='login'),
   url(r'^salir/$', LogoutView.as_view(),name='logout'),

#el name es para usar en las urls. junto con su n.s users, ej: users:login
]
