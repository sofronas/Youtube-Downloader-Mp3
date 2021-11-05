from __future__ import unicode_literals
import youtube_dl
print("******************************")
print("Youtube Downloader MP3")
print("Kleisimo patontas to 1")
print("******************************")
try:
     while True:
        video = input("video url:")
        if(video == "1"):
            break
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video])
except KeyboardInterrupt:
    print("Press 1 to quit")
#ydl_opts = {}

