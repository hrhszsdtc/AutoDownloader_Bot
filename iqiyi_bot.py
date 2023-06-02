#! usr/bin/python3
# coding:UTF-8

import http.client
import logging
import time
from urllib.parse import urlparse

logging.basicConfig(level=logging.DEBUG,

                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',

                    datefmt='%a, %d %b %Y %H:%M:%S',

                    filename='Downloader_%s.log' % (time.strftime('%Y-%m-%d')),

                    filemode='a')


class Downloader(object):
    # 文件下载器

    url = ''

    filename = ''


def __init__(self, full_url_str, filename):
    # 初始化

    self.url = urlparse(full_url_str)

    self.filename = filename


# To ZZH:这边几个判断语句是什么屎山!!!!
def download(self):
    '''''执行下载，返回True或False'''

    if self.url == '' or self.url == None or self.filename == '' or self.filename == None:
        logging.error('Invalid parameter for Downloader')

        return False

        successed = False

        conn = None

        if self.url.scheme == 'https':

            conn = http.client.HTTPSConnection(self.url.netloc)

        else:

            conn = http.client.HTTPConnection(self.url.netloc)

            conn.request('GET', self.url.path)

            response = conn.getresponse()

        if response.status == 200:

            total_size = response.getheader('Content-Length')

            total_size = (int)(total_size)

            if total_size > 0:

                finished_size = 0

            file = open(self.filename, 'wb')

            if file:

                progress = Progress()

            progress.start()

            while not response.closed:

                buffers = response.read(1024)

            file.write(buffers)

            finished_size += len(buffers)

            progress.update(finished_size, total_size)

            if finished_size >= total_size:

                break

            # ... end while statment

            file.close()

            progress.stop()

            progress.join()

        else:

            logging.error('Create local file %s failed' % (self.filename))

            # ... end if statment

    else:

        logging.error('Request file %s size failed' % (self.filename))

    # ... end if statment

else:

logging.error('HTTP/HTTPS request failed, status code:%d' % (response.status))

# ... end if statment

conn.close()

return successed

# ... end download() method

# ... end Downloader class


class DataWriter(threading.Thread):


filename = ''

data_dict = {'offset': 0, 'buffers_byte': b''}

queue = Queue(128)

__stop = False


def __init__(self, filename):


self.filename = filename

threading.Thread.__init__(self)


# Override


def run(self):


while not self.__stop:

self.queue.get(True, 1)


def put_data(data_dict):


# 将data_dict的数据放入队列，data_dict是一个字典，有两个元素：offset是偏移量，buffers_byte是二进制字节串


self.queue.put(data_dict)


def stop(self):


self.__stop = True


class Progress(threading.Thread):


interval = 1

total_size = 0

finished_size = 0

old_size = 0

__stop = False


def __init__(self, interval=0.5):


self.interval = interval

threading.Thread.__init__(self)


# Override


def run(self):


# logging.info(' Total Finished Percent Speed')


print(' Total Finished Percent Speed')

while not self.__stop:

time.sleep(self.interval)

if self.total_size > 0:

percent = self.finished_size / self.total_size * 100

speed = (self.finished_size - self.old_size) / self.interval

msg = '%12d %12d %10.2f%% %12d' % (
    self.total_size, self.finished_size, percent, speed)

# logging.info(msg)

print(msg)

self.old_size = self.finished_size

else:

logging.error('Total size is zero')


# ... end while statment

# ... end run() method


def stop(self):


self.__stop = True


def update(self, finished_size, total_size):


self.finished_size = finished_size

self.total_size = total_size


class TestDownloaderFunctions(unittest.TestCase):


def setUp(self):


print('setUp')


def test_download(self):


url = 'http://dldir1.qq.com/qqfile/qq/QQ8.4/18376/QQ8.4.exe'

filename = 'QQ8.4.exe'

dl = Downloader(url, filename)

dl.download()


def tearDown(self):


print('tearDown')

if __name__ == '__main__':

unittest.main()
