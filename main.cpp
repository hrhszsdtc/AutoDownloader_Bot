// Copyright (C) 2023 hrhszsdtc

#include <cstdlib>
#include <iostream>
#include <unistd.h>
#include <cstdio>
#include <cstring>

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

    // 获取系统类型
    SystemFlag systemFlag = getSystemFlag();
    // 定义命令
    string cmd;
    // 根据系统类型设置命令
    switch (systemFlag)
    {
    case SystemFlag::Windows:
        cmd = "py -3 ./src/main.py";
        break;
    case SystemFlag::Linux:
    case SystemFlag::MacOS:{
				   string whichCmd = "command -v python3";
				   FILE* pWhich  = popen(whichCmd.c_str(),"r");
				   if (!pWhich) {
					   cerr << "Command execution failed" << endl;
					   return EXIT_FAILURE;
				   }
				   char buf[256];
				   fgets(buf, sizeof(buf),pWhich);
				   pclose(pWhich);

				   if (strlen(buf) == 0){
					   cerr << "Python3 is not installed" << endl;
					   return EXIT_FAILURE;
				   }
				   buf[strlen(buf)-1] = '\0';

				   cmd = string(buf) + " ./src/main.py";
				   break;
			   }
    default:
        cerr << "Unsupported system." << endl;
        return EXIT_FAILURE;
    }

    FILE* pCmd = popen(cmd.c_str(), "r");
    if (!pCmd){
	    cerr << "Python3 in not installed or command execution failed." << endl;
	    return EXIT_FAILURE;
    }
    char buf[256];
    while (fgets(buf,sizeof(buf),pCmd)){
	    cout << buf;
    }
    pclose(pCmd);

    return EXIT_SUCCESS;
}
