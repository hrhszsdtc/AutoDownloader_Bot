# start.py

# ! usr/bin/python3
# coding:UTF-8

import sqlite3 as sql
import os
import sys
import time
import tkinter as tk
import urllib
import urllib.request
from pickle import dump, load

from constant import *
from std_output import *

"""
download_bot 主进程
ZZH Studio
"""
"""
 V0.0 Alpha
     :for test

 BUG report:
 Email:ZZH20081023@163.com
 by ZZH
"""

"""
脚本设置
"""

# 支持爬取的域名,注:全小写!!!
COULD_DOMAIN = ["baidu.com", "www.baidu.com", "v.qq.com"]

# 初始化语言
_PARSING = ""
_DOMAIN = ""
_DO_NOT_ABLE_TO_GET1 = ""
_FROM = ""
_TIP = ""
_TIP_TEXT = ""
_CHECK_URL = ""
_URL_UNAVAILABLE = ""
_CHECK_COMPLETED = ""
_START_SPIDER = ""
_INPUT_URL_ADDR = ""
_BREAKDOWN1 = ""
_BREAKDOWN2 = ""


# 多语言支持类
class Language(object):
    def __int__(self, data):
        self.data = data

    def import_language(self):
        with open("./configs/languages.conf", "r", encoding="utf-8") as config_file:
            lang_file_name = config_file.read()

        print(f">>{lang_file_name}")

        db = sql.connect(database=lang_file_name)

    def compile_lang_file(self, filename):
        """
        语言文件生成成员函数
        可以使用次函数生成语言文件，先再目录下创建文件***.lang，然后将完整文件名传入参数
        注意，data必须是list类型，且不可嵌套
        """
        print(f">>{self.data}")

        if not isinstance(self.data, list):
            pwarm("data isn't a list")

        else:
            try:
                with open(filename, "w", encoding="utf-8") as file:
                    # 序列化
                    dump(self.data, file)

            except Exception as e:
                pwarm(e)


# 导入语言
try:
    LANGUAGE = Language()
    LANGUAGE.import_language()

except Exception as e:
    error(f"语言导入失败！\n{e}")

    if PROTECT == "1":
        # 抛出异常退出程序
        sys.exit(1)

# 导入成功
pok("语言导入成功！")


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
        pwarm(e)


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
        pwarm(e)


# 解析url
def un_pack(url):
    print("\n")
    pout(f"正在解析:[{url}]")

    # 解析url
    temp = url[0:10]
    i = 0
    if "https://" in temp:  # 如果是https
        # 剥离域名
        i = 8
    else:
        i = 7
    temp = ""  # 清空缓存
    while True:
        ch = url[i]
        if ch == "/":
            break
        temp += ch
        i += 1

    # 打印分析出的域名
    domain = temp
    print(f"    domain:{domain}")

    # 查询是否支持爬取
    if domain not in COULD_DOMAIN:
        pwarm(f"报歉,该域名下[({domain}) from ({url})的资源暂时不支持爬取!")
        return -1
    # 调用爬虫脚本
    os.system(f"{PYTHON_COM} {domain}_bot.py {url}")
    # 将权限交由爬虫处理与调用


# 主程序
def main(mode, *url):
    cutline = "=" * 50
    cutline2 = "-" * 50
    if mode == 0:
        url = ""

        # 主界面
        print(f"{cutline}\n{ZZH}\n{cutline}\n")  # 打印ZZH图标
        print("\t:)Tip:输入exit退出,输入url地址开始爬取")
        while True:
            flag = 1
            url = input("URL: ")  # 输入URL

            if url == "exit":
                return 0  # 正常退出

            # 检查URL是否可用
            pout(f"Checking url[{url}]")

            try:
                respnse = urllib.request.urlopen(url)

            # 如果异常
            except urllib.request.URLError as e:
                print(f"URL不可用!\n:{e}")
                flag = 0
            except Exception as e:
                error(e)
                flag = 0
            # 如果可用
            if flag == 1:
                pok("URL Checking Over")

                # 爬取
                pout("Spider Start-up")
                un_pack(url)

            # 周期结束,打印分割线
            print(cutline2)


# GUI界面
def start_gui():
    # 创建主窗口
    window = tk.Tk()
    window.title("AutoSpider V1.0")

    # 显示消息控件
    text = tk.Text(window, height=10, width=50)  # ,state='disable')
    text.insert(tk.INSERT, ZZH2)
    text.pack()

    # 显示标签控件
    label = tk.Label(window, width=50, text="要爬取的URL地址:")
    label.pack()

    # 显示URL输入框
    url_entry = tk.Entry(window, width=50)
    url_entry.pack()

    window.mainloop()


def start(mode):
    command = ["nogui"]

    if mode == "gui":
        try:
            start_gui()

        except Exception as e:
            print(f"{e}\n:)程序非正常退出,可能是崩溃了!")
            print(
                '请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!'
            )

    elif mode == "nogui":
        try:
            if main(0) is None:
                print(":)程序非正常退出,可能是崩溃了!")
                print(
                    '请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!'
                )
        except Exception as e:
            print(f"{e}\n:)程序非正常退出,可能是崩溃了!")
            print(
                '请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!'
            )

    elif not (mode in command):
        pwarm(f"没有叫做{mode}的模式!")
        start_gui()

    else:
        start_gui()


if __name__ == "__main__":
    start("nogui")
