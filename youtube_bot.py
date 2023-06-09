import urllib.request

import pafy
from bs4 import BeautifulSoup

keyword = input("请输入链接channel后部分:")
channel_url = f'https://www.youtube.com/channel/{keyword}'

html_page = urllib.request.urlopen(channel_url)
soup = BeautifulSoup(html_page)
videos = []

for link in soup.findAll('a'):
    if link.get('href').startswith("/watch"):
        videos.append("https://www.youtube.com" + link.get('href'))

for video in videos:
    try:
        yt_video = pafy.new(video)
        title = yt_video.title
        description = yt_video.description

        print("\nTitle: " + title)
        print("Description: " + description)

    except Exception as e:
        print(e)
