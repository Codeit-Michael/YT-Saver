from django.urls import path
from . import views

urlpatterns = [
    path('',views.VideoProcessor.as_view(),name="video-processor"),
]
