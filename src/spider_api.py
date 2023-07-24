# !usr/bin/python3
# -*- coding:UTF-8 -*-
import os
import signal
import subprocess
import sys
import time
import tkinter as tk
import urllib
import urllib.request
from urllib.parse import urlparse

import constants
import utils


# 解析url
def un_pack(url):
    sys.stdout.write("\n")
    utils.pout(f"正在解析:[{url}]")

    # 解析url,打印分析出的域名
    domain = urlparse(url).netloc
    print(f"    domain:{domain}")
    if domain in constants.DOMAIN_NAME:
        try:
            domain_name = constants.DOMAIN_NAME[domain]
            # 调用爬虫脚本
            proc = subprocess.Popen(
                [PYTHON_COM, f"/script/{domain}.py", url], shell=True
            )
            proc.wait()
        except KeyboardInterrupt:
            proc.terminate()
            return
        except Exception as e:
            utils.perror(e)
            return
    else:
        utils.pwarm(f"抱歉,该域名下({domain}) from ({url})的资源暂时不支持爬取")
        return


# https操作库
class Spider:
    url = ""

    # 取得网页源代码
    def get_content(self):
        try:
            opener = urllib.request.build_opener()

            # 将伪装成的浏览器添加到对应的http头部
            opener.addheaders = [HEADERS]

            # 读取相应的url
            read_contend = opener.open(url).read()

            # 将获得的html解码为utf-8
            data = read_contend.decode("utf-8")

            # 打印源代码
            print(data)

        except Exception as e:
            utils.pwarm(e)

    def get_request(self):
        try:
            with urllib.request.urlopen(url) as f:
                data = f.read()
                print(f"Status:{f.status} {f.reason}")

                for k, v in f.getheaders():
                    print(f"{k}: {v}")
            print(f"Data:{data.decode('utf-8')}")

        except Exception as e:
            utils.pwarm(e)
