from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Song


# Create your views here.
def home(request):
    # landing page request and loading the artists to the page
    artists = Artist.objects.all()
    return render(request, 'index.html', {'artists': artists})


def explore(request):
    # page to display all the artists
    artists = Artist.objects.all()
    return render(request, 'explore.html', {'artists': artists})


def artist(request, pk):
    # page to display the artist page and info
    artist = Artist.objects.get(id=pk)
    return render(request, 'artistinfo.html', {'artist': artist})


def songs(request, pk):
    # page to display the songs
    artistic_name = Artist.objects.get(id=pk).artistic_name
    songs = Song.objects.filter(artist=pk)
    return render(request, 'songs.html', {'songs': songs, 'artistic_name': artistic_name})


def contact(request):
    # page to display the contact us page

    return render(request, 'contact_us.html')


def send_email(request):
    """
    uncomment the below code to allow the server to send mail
    once the server has a vail domain and domailmail to send from
    """
    # if request.method == 'POST':
    #     subject = request.POST.get('Name', '')
    #     message = request.POST.get('message', '')
    #     from_email = request.POST.get('email', '')
    #     if subject and message and from_email:
    #         try:
    #             send_mail(subject, message, from_email, ['wayneotemahegesa@gmail.com'])
    #         except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #         return HttpResponse('message sent.thanks')
    #     else:
    #         # In reality we'd use a form class
    #         # to get proper validation errors.
    #         return HttpResponse('Make sure all fields are entered and valid.')
    pass


