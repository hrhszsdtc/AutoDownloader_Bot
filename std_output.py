#! usr/bin/python3
# coding=utf-8
# 代码灰常简单，注释就不写了


LOG_FILE = "./log"


def log(str):
    file = open(LOG_FILE, 'a')
    file.write(str)
    file.close()
    return str


def pout(str):
    print(f"[*]\033[0;33m{str}\033[0m")
    log(f'[*]{str}\n')


def pwarm(str):
    print(f"\033[0;31m[!]{str}\033[0m")
    log(f'[!]{str}\n')


def error(str):
    print(f'-----------------------\
----\033[0;31mErrors\033[0m----------------------\
-----\n\t\033[0;31m{str}\033[0m\n\n-----------------------\
--------------------------------\
-----')
    log(f'[ERROR]{str}\n')


def pok(str):
    print(f"[ \033[0;32mOK\033[0m ] {str}")
    log(f'[ ok ]{str}\n')


# TEST
if __name__ == "__main__":
    log("----------TEST----------\n")
    pout("test")
    pwarm("test")
    error("test")
    pok("test")
    log("--------TESTOVER--------\n")
