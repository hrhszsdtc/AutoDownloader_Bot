#! usr/bin/python3
# coding=utf-8

def log(str):
    LOG_FILE = "./log"
    file = open(LOG_FILE, "a")
    file.write(str)
    file.close()
    return str


def pout(str):
    print(f"[*]\033[0;33m{str}\033[0m")
    log(f"[*]{str}\n")


def pwarm(str):
    print(f"\033[0;31m[!]{str}\033[0m")
    log(f"[!]{str}\n")


def error(str):
    print(
        f"-----------------------\
----\033[0;31mErrors\033[0m----------------------\
-----\n\t\033[0;31m{str}\033[0m\n\n-----------------------\
--------------------------------\
-----"
    )
    log(f"[ERROR]{str}\n")


def pok(str):
    print(f"[ \033[0;32mOK\033[0m ] {str}")
    log(f"[ ok ]{str}\n")
