import re
from django.shortcuts import render, redirect
from pytube import YouTube

# Create your views here.
def home(request):
    myTitle = ''
    myQuality = None
    if request.method == 'POST':
        link = request.POST['given_url']
        myVideo = YouTube(link)
        myTitle = myVideo.title
        myQuality = myVideo.streams        
    context = {'vid':myTitle,'qual':myQuality}
    return render(request,'app/home.html',context)

# PROBLEM: HOW TO SELECT AND DOWNLOAD THE RESOLUTION CHOSEN