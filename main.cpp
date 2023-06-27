#include <cstdlib>
#include <iostream>
#include <unistd.h>
#include <cstdio>

using namespace std;

enum SystemFlag {
    Windows,
    Linux,
    MacOS,
    Other
};

SystemFlag getSystemFlag() {
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

int main() {
    const string pythonCmd = "python3 ./src/main.py";
    const string envCmd = "ENV.exe \\src\\main.py";

    SystemFlag systemFlag = getSystemFlag();
    string cmd;
    switch (systemFlag) {
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

    if (access(cmd.c_str(), F_OK) == -1) {
        cerr << "Python3 is not installed." << endl;
        return EXIT_FAILURE;
    }

    int ret = std::system(cmd.c_str());
    if (ret == -1) {
        perror("Command execution failed");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
