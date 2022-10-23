from django.urls import path
from . import views

urlpatterns = [
    path('Video-Downloader', views.YTDownloader, name='YTDownloader'),
    path('Video-Downloader-Streams', views.getStreams, name='YTgetStreams'),
    path('Download', views.downloadVideo, name='DownloadVideo')
]
