import random
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

user_agents = []
with open('./conf/user_agents.txt') as f:
    lines = f.readlines()
    for line in lines:
        user_agents.append(line.strip('\n'))
user_agent = random.choice(user_agents)
print(user_agent)
keyword = input("请输入视频BV号:")
url = f'https://www.bilibili.com/video/BV{keyword}/'
