#! usr/bin/python3
# coding:UTF-8

"""
download_bot 主进程

"""

# by ZZH

from std_output import *  # 软件标准输出库
import tkinter as tk
import re
from time import sleep
import bs4
import os
import urllib

import std_output

# 系统下调用python的命令
PYTHON_COM = 'python3'

# 支持爬取的域名,注:全小写!!!
COULD_DOMAIN = ['baidu.com', 'www.baidu.com', 'v.qq.com']

ZZH = "\
      __________\t  __________\t       ___    ___\n\
     /_________/|\t /_________/|\t      /  /|  /  /|\n\
     |_______  |^\t |_______  |^\t     /  /_/_/  / /\n\
           /  / / \t       /  / /\t    /  ____   / /\n\
         /  / /  \t     /  / /\t   /  / | /  / /\n\
       /  / /___\t   /  / /___\t  /  / / /  / /\n\
     /  /______/|\t /  /______/|\t /__/ / /__/ /\n\
    |__________|/\t|__________|/\t |__|/  |__|/\n"
# V0.1 Alpha
# for test

# BUG report:
# Email:ZZH20081023@163.com


# 解析url


def un_pack(url):
	print('\n')
	pout(f"正在解析:[{url}]")

	# 解析url
	temp = url[0:10]
	i = 0
	if 'https://' in temp:  # 如果是https
	# 剥离域名
		i = 8
	else:
		i = 7
	temp = ''  # 清空缓存
	while True:
		ch = url[i]
		if ch == '/':
			break
		else:
			temp += ch
		i += 1

    # 解析url
    temp = url[0:10]
    i = 0
    if 'https://' in temp:  # 如果是https
        # 剥离域名
        i = 8
    else:
        i = 7
    temp = ''  # 清空缓存
    while True:
        ch_ar = url[i]
        if ch_ar == '/':
            break
        temp += ch_ar
        i += 1
	#打印分析出的域名
	domain = temp
	print(f'    domain:{domain}')

	#查询是否支持爬取
	if (domain in COULD_DOMAIN) == False:
		pwarm(f'报歉,该域名下[({domain}) from ({url})的资源暂时不支持爬取!')
		return -1
	#调用爬虫脚本
	os.system(f"{PYTHON_COM} {domain}_bot.py {url}")
	#将权限交由爬虫处理与调用
	
#主程序
def main(mode,*url):
	cutline = '='*60
	cutline2 = '-'*60
	if mode == 0:

		url = ''

		#主界面
		print(f'{cutline}\n\n\n\
{ZZH}\n\n\n\
{cutline}\n')		#打印ZZH图标
		print('\t:)Tip:输入exit退出,输入url地址开始爬取')
		while True:
			flag = 1
			url = input('URL: ')	#输入URL	
			
			if url == 'exit':
				return 0			#正常退出
			
			#检查URL是否可用
			pout(f'Checking url[{url}]')
			
			try:
				respnse = urllib.request.urlopen(url)
			
			#如果异常
			except urllib.request.URLError as e:
				print(f"URL不可用!\n:{e}")
				flag = 0
			except Exception as e:
				error(e)
				flag = 0
			#如果可用
			if flag == 1:
				
				pok('URL Checking Over')
				
				#爬取
				print('[*]Spider Start-up')
				un_pack(url)
			
			#周期结束,打印分割线
			print(cutline2)

#GUI界面
def start_gui():
	#创建主窗口
	window = tk.Tk()
	window.title("AutoSpider V1.0")
	
	#显示消息控件
	text = tk.Text(window,height=10,width=50)
	text.pack()
	
	#显示标签控件
	label = tk.Label(window,width=50,text='要爬取的URL地址:')
	label.pack()
	
	#显示URL输入框
	url_entry = tk.Entry(window,width=50)
	url_entry.pack()
	
	window.mainloop()
	

def start(mode):
	
	command = ['nogui']
	
	if mode == 'gui':
		try:
			start_gui()
			
		except Exception as e:
			print(f"{e}\n:)程序非正常退出,可能是崩溃了!")
			print('请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!')
	
	elif mode == 'nogui':
		try:
			if main(0) == None:
				print(":)程序非正常退出,可能是崩溃了!")
				print('请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!')
		except Exception as e:
			print(f"{e}\n:)程序非正常退出,可能是崩溃了!")
			print('请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!')
	
	elif not(mode in command):
		pwarm(f"没有叫做{mode}的模式!")
		start_gui()
	
	else:
		start_gui()

if __name__ == "__main__":
	start('gui')
