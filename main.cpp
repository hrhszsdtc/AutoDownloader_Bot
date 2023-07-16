// Copyright (C) 2023 hrhszsdtc

#include <cstdlib>
#include <iostream>
#include <unistd.h>
#include <cstdio>

using namespace std;

enum SystemFlag
{
    Windows,
    Linux,
    MacOS,
    Other
};

SystemFlag getSystemFlag()
{
#ifdef _WIN32
    return SystemFlag::Windows;
#elif __APPLE__
    return SystemFlag::MacOS;
#elif __linux__
    return SystemFlag::Linux;
#else
    return SystemFlag::Other;
#endif
}

int main()
{
    // 定义python命令
    const string pythonCmd = "python3 ./src/main.py";
    // 定义环境命令
    const string envCmd = "py -3 \\src\\main.py";

    // 获取系统类型
    SystemFlag systemFlag = getSystemFlag();
    // 定义命令
    string cmd;
    // 根据系统类型设置命令
    switch (systemFlag)
    {
    case SystemFlag::Windows:
        cmd = envCmd;
        break;
    case SystemFlag::Linux:
        cmd = pythonCmd;
        break;
    case SystemFlag::MacOS:
        cmd = pythonCmd;
        break;
    default:
        cerr << "Unsupported system." << endl;
        return EXIT_FAILURE;
    }

    // 检查python是否可执行
    if (access(cmd.c_str(), X_OK) == -1)
    {
        cerr << "Python3 is not installed." << endl;
        return EXIT_FAILURE;
    }

    // 执行命令
    int ret = std::system(cmd.c_str());
    if (ret == -1)
    {
        perror("Command execution failed");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
