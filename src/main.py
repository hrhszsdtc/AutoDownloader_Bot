# Copyright (C) 2023 hrhszsdtc

import os
import sys
import time
import tkinter as tk
import urllib
import urllib.request
from urllib.parse import urlparse

import utils
import constants

# 版权信息
copyright_notice = "Copyright (C) 2023 hrhszsdtc"

"""
脚本设置
"""

# 域名映射字典
DN = {
    "bilibili": ("bilibili.com", "www.bilibili.com", "b23.tv"),
    "iqiyi": ("www.iqiyi.com", "iqiyi.com"),
}
DOMAIN_NAME = {x: k for k, v in DN.items() for x in v}

# 取得网页源代码
def get_content(url_path):
    try:
        opener = urllib.request.build_opener()

        # 将伪装成的浏览器添加到对应的http头部
        opener.addheaders = [HEADERS]

        # 读取相应的url
        read_contend = opener.open(url_path).read()

        # 将获得的html解码为utf-8
        data = read_contend.decode("utf-8")

        # 打印源代码
        print(data)

    except Exception as e:
        utils.pwarm(e)


# 用于获得HTTP响应头和JSON数据
def get_request(url):
    try:
        with urllib.request.urlopen(url) as f:
            data = f.read()
            print(f"Status:{f.status} {f.reason}")

            for k, v in f.getheaders():
                print(f"{k}: {v}")
        print(f"Data:{data.decode('utf-8')}")

    except Exception as e:
        utils.pwarm(e)


# 解析url
def un_pack(url):
    print("\n")
    utils.pout(f"正在解析:[{url}]")

    # 解析url,打印分析出的域名
    domain = urlparse(url)
    print(f"    domain:{domain}")

    try:
        domain_name = DOMAIN_NAME[domain]
        # 调用爬虫脚本
        os.system(f"{PYTHON_COM} /script/{domain}.py {url}")
        # 将权限交由爬虫处理与调用
    except:
        utils.pwarm(f"抱歉,该域名下({domain}) from ({url})的资源暂时不支持爬取")
        return -1


# 主程序
def main(mode, *url):
    cutline = "=" * 50
    cutline2 = "-" * 50
    if mode == 0:
        url = ""

        # 主界面
        print(f"{cutline}\n{copyright_notice}\n{cutline}\n")  # 打印版权信息
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
                print(f"URL不可用!\n:{e}")
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


# GUI界面
def start_gui():
    # 创建主窗口
    window = tk.Tk()
    window.title("AD_B by hrhszsdtc")

    # 显示消息控件
    text = tk.Text(window, height=10, width=50)  # ,state='disable')
    text.insert(tk.INSERT, copyright_notice)
    text.pack()

    # 显示标签控件
    label = tk.Label(window, width=50, text="要爬取的URL地址:")
    label.pack()

    # 显示URL输入框
    url_entry = tk.Entry(window, width=50)
    url_entry.pack()

    window.mainloop()


def start(mode):
    command = ["nogui","gui"]

    if mode == "gui":
        try:
            start_gui()

        except Exception as e:
            print(f"{e}\n:)程序非正常退出,可能是崩溃了!")
            print(
                '请向tech-whimsy@outlook.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!'
            )

    elif mode == "nogui":
        try:
            if main(0) is None:
                print(":)程序非正常退出,可能是崩溃了!")
                print(
                    '请向tech-whimsy@outlook.com发送标题为"Bug Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您的反馈!'
                )
        except Exception as e:
            print(f"{e}\n:)程序非正常退出,可能是崩溃了!")
            print(
                '请向tech-whimsy@outlook.com发送标题为"Bug Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您的反馈!'
            )

    elif not (mode in command):
        utils.pwarm(f"没有叫做{mode}的模式!")
        start_gui()

    else:
        start_gui()


if __name__ == "__main__":
    model = input("请输入模式(nogui/gui):")
    start(model)
