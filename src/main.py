# Copyright (C) 2023 hrhszsdtc

import contextlib
import os
import signal
import subprocess
import sys
import time
import tkinter as tk
import urllib
import urllib.request
from urllib.parse import urlparse

from constants import *
from utils import *
from gui import *
from SpiderZFramework import *



# 主程序
def main(mode, *url):
    cutline = "=" * 50
    cutline2 = "-" * 50
    if mode == 0:
        url = ""

        # 主界面
        sys.stdout.write(f"{cutline}\n{copyright_notice}\n{cutline}\n")  # 打印版权信息
        print("\t:)Tip:输入exit退出,输入url地址开始爬取")
        while True:
            flag = 1
            url = input("URL: ")  # 输入URL

            if url == "exit":
                return 0  # 正常退出

            # 检查URL是否可用
            utils.pout(f"Checking url[{url}]")

            try:
                respnse = urllib.request.urlopen(url)

            # 如果异常
            except urllib.request.URLError as e:
                sys.stdout.write(f"URL不可用!\n:{e}")
                flag = 0
            except Exception as e:
                utils.perror(e)
                flag = 0
            # 如果可用
            if flag == 1:
                utils.pok("URL Checking Over")

                # 爬取
                utils.pout("Spider Start-up")
                un_pack(url)

            # 周期结束,打印分割线
            print(cutline2)


def start(mode):
    command = ["nogui", "gui"]

    if mode == "gui":
        try:
            start_gui()

        except Exception as e:
            sys.stdout.write(f"{e}\n:)程序非正常退出,可能是崩溃了!")
            utils.feedback()

    elif mode == "nogui":
        try:
            if main(0) is None:
                print(":)程序非正常退出,可能是崩溃了!")
                utils.feedback()
        except Exception as e:
            sys.stdout.write(f"{e}\n:)程序非正常退出,可能是崩溃了!")
            utils.feedback()

    elif not (mode in command):
        utils.pwarm(f"没有叫做{mode}的模式!")
        start_gui()

    else:
        start_gui()

        
if __name__ == "__main__":
    try:
        model = sys.argv[1]
    except Exception as e:
        utils.pwarm(e)
        model = "nogui"
    finally:
        start(model)
