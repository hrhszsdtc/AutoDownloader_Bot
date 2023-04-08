import urllib.parse
import urllib.request

keyword = input("请输入视频BV号:")
url = "https://www.bilibili.com/video/BV" + quote(keyword)
print(url)