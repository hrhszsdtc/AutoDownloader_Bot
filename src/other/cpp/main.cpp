// Copyright (C) 2023 hrhszsdtc

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <stdexcept>
#include <string>
#include <fstream>
#include <sstream>
#include <filesystem>

using namespace std;

enum class SystemFlag
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

string getPythonCmd()
{
    switch (getSystemFlag())
    {
        case SystemFlag::Windows:
            return "python";
        case SystemFlag::Linux:
        case SystemFlag::MacOS:
        {
            string pythonPath;
            try {
                pythonPath = filesystem::read_symlink("/usr/bin/python3").string();
            } catch (filesystem::filesystem_error& e) {
                throw runtime_error("Python3 is not installed");
            }
            return pythonPath;
        }
        default:
            throw runtime_error("Unsupported system.");
    }
}

int main()
{
    // 定义python命令
    const string pythonCmd = getPythonCmd();

    // 输出python命令
    cout << "Python command: " << pythonCmd << endl;

    return EXIT_SUCCESS;
}

