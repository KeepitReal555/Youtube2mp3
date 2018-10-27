import os
import ssl

import youtube_dl


ssl._create_default_https_context = ssl._create_unverified_context
os.environ["HTTPS_PROXY"] = 'http://127.0.0.1:1087/'
os.environ["HTTP_PROXY"] = 'https://127.0.0.1:1087'


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=IhzUY1W7qUM'])