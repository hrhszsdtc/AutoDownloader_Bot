# Copyright (C) 2023 hrhszsdtc

import os
import sys
"""
主程序常量库
"""

# 系统下调用python的命令
PYTHON_COM = "python"

# 系统类型，填1代表WINDOWS，填2为LINUX或UNIX
SYSTEM = 1
if SYSTEM not in {1, 2}:
    # 抛出异常退出程序
    sys.exit(1)
if SYSTEM == 2:
    PYTHON_COM = "python3"

# 默认语言：中文
zh_cn = [
    "正在解析",
    "域名",
    "报歉,该域名下",
    "来自",
    "的资源暂时不支持爬取",
    "提示",
    "输入exit退出,输入url地址开始爬取",
    "检查URL",
    "URL不可用",
    "URL检查完毕",
    "启动网络爬虫",
    "要爬取的URL地址",
    "程序非正常退出,可能是崩溃了",
    '请向tech-whimsy@outlook.com发送标题为"BugReport"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您的反馈!',
    "没有叫做",
    "的模式",
]

# 伪装成浏览器(此处伪装成chrome)
HEADERS = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
)

# 日志文件名
LOG_FILE = "../log"

# 脚本保护
script_path = os.path.dirname(__file__)
file_path = os.path.join(script_path, "config", "protect.conf")
file = open(file_path, "r")
PROTECT = file.readline()
if not (PROTECT in {"0", "1"}):
    print(f"CONFIG ERROR:./config/protect.conf can't be {PROTECT}")
    sys.exit(1)
file.close()
