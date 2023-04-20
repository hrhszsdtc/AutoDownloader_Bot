from urllib import request

import chardet
import requests


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

		pass

		'''

        # 写入文件

        file = open(root+filename, 'w')  # 以写的方式打开文件

        file.write(data)  # 写入数据

        file.close()  # 关闭文件

        return 0


def main():

    # 获得视频BV号

    keyword = '1Na4y1T75k'  # input("请输入视频BV号:")

    # 合成为目标URL

    url = f'https://www.bilibili.com/video/BV{keyword}/'

    get_request(url, 0)


if __name__ == '__main__':

    main()
