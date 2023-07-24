import tkinter as tk
import signal
import subprocess
import contextlib
import os

from constants import *
from utils import *
from SpiderZFramework import *

# GUI界面
class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("AD_B by hrhszsdtc")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建一个子窗口
        self.sub_frame = tk.Frame(self)
        # 创建一个文本框
        self.text = tk.Text(self.sub_frame)
        # 添加版权信息
        self.text.insert(tk.INSERT, copyright_notice)
        # 创建一个滚动条
        self.scroll = tk.Scrollbar(self.sub_frame)
        # 设置滚动条的滚动范围
        self.text.config(yscrollcommand=self.scroll.set)
        # 设置滚动条的滚动事件
        self.scroll.config(command=self.text.yview)
        # 绑定滚动条的滚动事件
        self.text.grid(row=0, column=0, sticky="nsew")
        self.scroll.grid(row=0, column=1, sticky="ns")
        # 将子窗口放入窗口中
        self.sub_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # 创建一个标签
        self.label = tk.Label(
            self, text="Type in the URL,press <Enter> to start and <Ctrl+C> to end."
        )
        # 将标签放入窗口中
        self.label.grid(row=1)

        # 创建一个输入框
        self.url_entry = tk.Entry(self)
        # 将输入框放入窗口中
        self.url_entry.grid(row=2)

        # 绑定输入框的回车事件
        self.url_entry.bind("<Return>", lambda event: un_pack(self.url_entry.get()))


class PrintToText:
    def __init__(self, text):
        self.text = text

    def write(self, s):
        # 将字符串插入文本框中
        self.text.insert(tk.END, s)
        # 滚动到文本框末尾
        self.text.see(tk.END)
        # 更新文本框
        self.text.update()


# 定义开始GUI函数
def start_gui():
    # 创建Tk实例
    root = tk.Tk()
    # 创建GUI实例
    gui = GUI(master=root)
    # 创建PrintToText实例
    ptt = PrintToText(gui.text)
    # 把PrintToText实例把输出放入Tk实例
    with contextlib.redirect_stdout(ptt), contextlib.redirect_stderr(ptt):
        # 运行GUI实例
        gui.master.mainloop()


