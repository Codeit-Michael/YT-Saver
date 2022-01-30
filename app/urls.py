from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name="home"),
]

# urlpatterns = [
#     path('',views.home,name='home'),
#     path('bobo/<str:id>/<str:url>/',views.downloadVid,name='downloadVid'),
# ]