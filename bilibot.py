import urllib.parse
import urllib.request

keyword = input("请输入视频BV号:")
url = "https://www.bilibili.com/video/BV" + urllib.parse.quote(keyword)
response = urllib.request.urlopen(url)
print(response.read().decode("utf-8"))
