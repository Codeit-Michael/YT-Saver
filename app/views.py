from urllib import request
from django.shortcuts import render, redirect
from pytube import YouTube
from django.views.generic import View

# Create your views here.
class home(View):
    def __init__(self,url=None):
        self.url = url

    def get(self,request):
        # print(self.url)
        return render(request,'app/home.html')    

    def post(self,request):
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            vidTitle,vidThumbnail = video.title,video.thumbnail_url
            qual,stream = [],[]
            for vid in video.streams.filter(progressive=True):
                qual.append(vid.resolution)
                stream.append(vid)
            context = {'vidTitle':vidTitle,'vidThumbnail':vidThumbnail,
                        'qual':qual,'stream':stream,
                        'url':self.url}
            return render(request,'app/home.html',context)

        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            stream = [x for x in video.streams.filter(progressive=True)]
            video.streams[int(request.POST.get('download-vid')) - 1].download(output_path='../../Downloads')

        return render(request,'app/home.html')
