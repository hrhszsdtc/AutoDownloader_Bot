// Launcher.cpp
//-*- coding:UTF-8 -*-

#include <cstdlib>
#include <iostream>

using namespace std;

/***************************************
这是AutoDownload Bot的启动程序
编译环境：gcc
作者:ZZH

V1.0.0 Beta
***************************************/

#define SYSTEMFLAG "MSNT"
//  在这里输入你的系统类型，"MSNT"代表微软
//  的以NT为内核的系统 如Windows 7/8/10/11
//  "*nix"代表类UNIX系统，包括但不限于UNIX、
//  基于Linux内核的桌面版、发行版、服务器版
//  操作系统

#if SYSTEMFLAG == "MSNT"                // NT内核系统？
#define COMMAND "ENV.exe \\bin\\bot.py" // 设置命令
#pragma comment(                                                               \
    linker,                                                                    \
    "/subsystem:\"windows\" /entry:\"mainCRTStartup\"") // 设置入口地址

#elif SYSTEMFLAG == "*nix"             // 类UNIX系统？
#define COMMAND "python3 ./bin/bot.py" // 设置命令

#else               // 输入错误
#define COMMAND "0" // 返回异常

#endif

int main() {

  if (COMMAND == "0")
    return 0;

  else
    system(COMMAND);

  return 0;
}
