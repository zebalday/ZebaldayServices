from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
from .conversiones import segToMins
import os

# Create your views here.

# Landing page for downloading a video.
def YTDownloader(request):

    return render(request, "YTDownloader/VideoDownloader.html",{
        'Title':'Video Downloader'
    })
        
# Get Video and download Streams info. Also handle errors.
def getStreams(request):

    if request.method == 'GET':
        
        link = request.GET['Link']
        link = str(link.strip())

        try:
            
            # VIDEO INFORMATION
            yt = YouTube(link)
            video = {
                'Title': yt.title,
                'Length': segToMins(yt.length),
                'Views': yt.views,
                'Thumbnail': yt.thumbnail_url,
                'Link': link
            }


            # GETTING STREAMS INFO

            raw_streams = yt.streams.order_by('itag').filter(file_extension='mp4')
            raw_streams = raw_streams[:3]

            streams = []

            for stream_raw in raw_streams:
                
                itag = int(getattr(stream_raw, 'itag'))
                resolution = str(stream_raw.resolution)
                size = str(round(getattr(stream_raw, 'filesize')/1000000, 2))

                stream = {
                    'ID': itag,
                    'Resolution': resolution,
                    'Size': size
                }

                streams.append(stream)

            
            # RETURN TO LANDING PAGE WITH THE INFO
            return render(request, "YTDownloader/VideoDownloader.html",{
                'Title':'Video Downloader',
                'Video': video,
                'Streams': streams
            })

        except Exception as e:
            return render(request, "YTDownloader/VideoDownloader.html",{
                'Title':'Video Downloader',
                'Error': True
            })

# Download the Stream.
def downloadVideo(request):

    if request.method == 'POST':
        url = request.POST['video-link']
        itag = request.POST['stream-id']

        try:

            # Downloading video.
            yt = YouTube(url)
            stream = yt.streams.get_by_itag(itag)            
            stream.download(output_path = 'Media\YTVideos')
            
            # Opening folder after complete download.
            stream.on_complete("Media\YTVideos")
            path = os.path.abspath("Media\YTVideos")
            os.startfile(path)

            # Returning to landing page.
            return render(request, "YTDownloader/VideoDownloader.html",{
                'Title': 'Video Downloader',
                "Donwloaded": True
            })

        except Exception as e:
            return render(request, "YTDownloader/VideoDownloader.html",{
                'Title':'Video Downloader',
                'Error': True
            })


        