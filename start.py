#! usr/bin/python3
#coding:UTF-8

#by ZZH

#支持爬取的域名,注:全小写!!!
COULD_DOMAIN = ['baidu.com']

ZZH="\
      __________\t  __________\t       ___    ___\n\
     /_________/|\t /_________/|\t      /  /|  /  /|\n\
     |_______  |^\t |_______  |^\t     /  /_/_/  / /\n\
           /  / / \t       /  / /\t    /  ____   / /\n\
         /  / /  \t     /  / /\t   /  / | /  / /\n\
       /  / /___\t   /  / /___\t  /  / / /  / /\n\
     /  /______/|\t /  /______/|\t /__/ / /__/ /\n\
    |__________|/\t|__________|/\t |__|/  |__|/\n"
#iqiyi_Bot V0.1 Alpha
#Just for test

#BUG report:
#Email:ZZH20081023@163.com

import urllib
import bs4
from time import sleep
import re

def get_request(url, flag, *file_root):
    '''
    用于http/https协议下的get请求
    url代表要请求的url,flag为返回方式:
            若flag为0,则返回明文或2进制数据
            若flag为1,则将得到的数据写入文件
    file_root为选填参数,代表请求的数据储存是时的目录,默认为'./'
    '''

    try:
        response = request.urlopen(url)
    except:
        print('[!]请求URL下的数据异常')
        return -1  # 将函数以异常形式返回错误代

    response = requests.get(url)  # 获取响应
    data = response.content  # 获取响应内容
    result = chardet.detect(data)  # 计算权重
    encoding = result["encoding"]  # 获取编码类型
    content = data.decode(encoding, errors='replace')  # 解码

    if flag == 0:  # 以明文或数据输出并且返回
        print(content)  # 打印数据
        return content  # 返回数据

    elif flag == 1:  # 将数据写入文件
        root = ''
        if file_root == None:  # 如果未传递参数
            root = './'  # 设置为默认目录
        else:  # 如果传入参数
            root = file_root  # 设置目录
            
        # 获得文件名
        '''
		这里没写完
		'''
		
        # 写入文件
        file = open(root+filename, 'w')  # 以写的方式打开文件
        file.write(data)  # 写入数据
        file.close()  # 关闭文件
        return 0

def un_pack(url):
	print(f"\n[*]正在解析:[{url}]")
    
	#解析url
	temp = url[0:10]
	i = 0
	if 'https://' in temp:#如果是https
	#剥离域名
		i = 8
	else:
		i = 7
	temp = ''			#清空缓存
	while True:
		ch = url[i]
		if ch == '/':
			break
		else:
			temp += ch
		i += 1

	#打印分析出的域名
	domain = temp
	print(f'    domain:{domain}')

	#查询是否支持爬取
	if domain in COULD_DOMAIN == False:
		print(f'[!]抱歉,该域名下[({doamin}) from (\
{url})的资源暂时不支持爬取!')
		return
    #获取域名

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
			print(f'[*]Checking url[{url}]')
			
			try:
				respnse = urllib.request.urlopen(url)
			
			#如果异常
			except urllib.request.URLError as e:
				print(f"\033[0;33m[!]URL不可用!\n\033[0m\
\033[0;31m  :){e}\033[0m")
				flag = 0
			except Exception as e:
				print(f'-----------------------\
----\033[0;31mErrors\033[0m----------------------\
-----\n\t\033[0;31m{e}\033[0m\n\n')
				flag = 0
			#如果可用
			if flag == 1:
				
				print('[ \033[0;32mOK\033[0m ] URL Checking Over')
				
				#爬取
				print('[*]Spider Start-up')
				un_pack(url)
			
			#周期结束,打印分割线
			print(cutline2)

if __name__ == '__main__':
	try:
		if main(0) == None:
			print("\f\f:)程序非正常退出,可能是崩溃了!")
			print('\t请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!')
	except Exception as e:
		print(f"{e}\f\f:)程序非正常退出,可能是崩溃了!")
		print('\t请向ZZH20081023@163.com发送标题为"Bu\
g Report"的邮件,并复制报错信息以及崩溃前的具体操作,感谢您\
的反馈!')
#未完成
