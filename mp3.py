# from __future__ import unicode_literals
# import youtube_dl
# print("******************************")
# print("Youtube Downloader MP3")
# print("Kleisimo patontas to 1")
# print("******************************")
# try:
#      while True:
#         video = input("video url:")
#         if(video == "1"):
#             break
#         ydl_opts = {
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }],
#         }
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([video])
# except KeyboardInterrupt:
#     print("Press 1 to quit")
# #ydl_opts = {}

# New version: (yt-dlp==2025.6.25)
from __future__ import unicode_literals
import yt_dlp as youtube_dl

print("******************************")
print("Youtube Downloader MP3")
print("Kleisimo patontas to 1")
print("******************************")

try:
    while True:
        video = input("video url:")
        if video.strip() == "1":
            break

        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
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
