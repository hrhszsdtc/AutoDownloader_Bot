import urllib.parse
import urllib.request

keyword = input("请输入视频BV号:")
url = f'https://www.bilibili.com/video/BV{keyword}/'
response = urllib.request.urlopen(url)
print(response.read().decode('utf-8'))
