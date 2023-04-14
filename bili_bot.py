import random
import socket
import urllib.parse
import urllib.request

import socks  # pip install PySocks
from bs4 import BeautifulSoup

# useragent
user_agents = []
with open('./conf/user_agents.txt') as f:
    lines = f.readlines()
    for line in lines:
        user_agents.append(line.strip('\n'))
user_agent = random.choice(user_agents)

# proxy(needs tor service)
socks.set_default_proxy(socks.SOCK5, "localhost", 9150)
socket.socket = socks.socksocket

# 主体
keyword = input("请输入视频BV号:")
url = f'https://www.bilibili.com/video/BV{keyword}/'
