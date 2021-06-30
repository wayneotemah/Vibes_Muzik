from django.urls import path, re_path
from . import views

# created a url file for the vibes app to map out all the routes in the app

urlpatterns = [
    path('', views.home, name='home'),
    path(r'explore', views.explore, name='explore'),
    path(r'songs/<pk>', views.songs, name='songs'),
    path(r'contact', views.contact, name='contact'),
    path(r'<pk>', views.artist, name='artist'),
    path(r'send_email', views.send_email, name='send_email')

]