#! usr/bin/python3

def pout(str):
	print(f"[*]\033[0;33m{str}\033[0m")

def pwarm(str):
	print(f"\033[0;31m[!]{str}\033[0m")

def error(str):
	print(f'-----------------------\
----\033[0;31mErrors\033[0m----------------------\
-----\n\t\033[0;31m{str}\033[0m\n\n-----------------------\
--------------------------------\
-----')

def pok(str):
	print(f"[\033[0;32mOK\033[0m ] {str}")
#TEST
if __name__ == "__main__":
	pout("sss")
	pwarm("sss")
	error("sss")
	pok("sss")
