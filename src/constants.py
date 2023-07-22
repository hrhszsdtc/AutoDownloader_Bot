# Copyright (C) 2023 hrhszsdtc

import os
import random
import sys

import utils

# 版权信息
copyright_notice = "Copyright (C) 2023 hrhszsdtc"

# 反馈事项
feedback_notice = "请联系hrhszdtc团队(https://github.com/hrhszsdtc)并发送反馈报告,报告应包含:\n1. 使用的程序和运行环境\n2. 系统版本\n3. 报错信息\n4. 报错前的操作\n5. 其他可能的信息\n感谢您的反馈!"

script_path = os.path.abspath(__file__)
script_folder = os.path.dirname(script_path)
script_name = os.path.basename(script_folder)
if script_name == "src":
    pass
else:
    src_path = os.path.join(script_path, "src")
    if os.path.exists(src_path):
        os.chdir(src_path)
    else:
        raise FileNotFoundError("src folder not found")

try:
    PYTHON_COM = sys.executable
except AttributeError as e:
    utils.perror(f"{e}:Python3 is not installed.")
    sys.exit(-1)

# UserAgent
with open("config/user_agents.txt", "r", encoding='utf-8') as f:
    HEADERS = f.readlines()
    HEADER = random.choice(HEADERS)

# 日志文件名
LOG_FILE = "../log"
