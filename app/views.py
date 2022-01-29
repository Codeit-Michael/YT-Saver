import re
from django.shortcuts import render, redirect
from pytube import YouTube

# Create your views here.
def home(request,*args,**kwargs):
    if request.method == 'POST':
        url = request.POST['given_url']
        video = YouTube(url)
        vidTitle,vidThumbnail = video.title,video.thumbnail_url
        qual,stream = [],[]
        for vid in video.streams.filter(progressive=True):
            qual.append(vid.resolution)
            stream.append(vid)
        context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                    'qual':qual,'stream':stream,
                    'url':url}
        return render (request,'app/home.html',context)

    return render (request,'app/home.html')


# def downloadVid(request,id:str,stream:list):
#     print(id,stream)
#     return redirect('home')

# PROBLEM: HOW TO SELECT AND DOWNLOAD THE RESOLUTION CHOSEN