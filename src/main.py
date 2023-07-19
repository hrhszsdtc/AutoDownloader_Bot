# Copyright (C) 2023 hrhszsdtc

import os
import sys
import signal
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
    except:
        utils.pwarm(f"抱歉,该域名下({domain}) from ({url})的资源暂时不支持爬取")
        return

def un_pack_gui(input_url):
    try:
        un_pack(input_url)
    except KeyboardInterrupt:
        return

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

def print_to_text(text):
    def write(s):
        text.insert(tk.END, s)
        text.see(tk.END)
        text.update()
    return write

# GUI界面
class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("AD_B by hrhszsdtc")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.sub_frame = tk.Frame(self)
        self.text = tk.Text(self.sub_frame)
        self.text.insert(tk.INSERT, copyright_notice)
        self.scroll = tk.Scrollbar(self.sub_frame)
        self.text.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text.yview)
        self.text.grid(row=0, column=0, sticky="nsew")
        self.scroll.grid(row=0, column=1, sticky="ns")
        self.sub_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        sys.stdout = print_to_text(self.text)
        sys.stderr = print_to_text(self.text)

        self.label = tk.Label(self, text="Type in the URL,press Enter to start and Ctrl+C to end.")
        self.label.grid(row=1)

        self.url_entry = tk.Entry(self)
        self.url_entry.grid(row=2)

        user_input = self.url_entry.get()
        self.url_entry.bind("<Return>", lambda event:un_pack_gui(user_input))
def start_gui():
    root = tk.Tk()
    gui = GUI(master=root)
    gui.mainloop()

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
