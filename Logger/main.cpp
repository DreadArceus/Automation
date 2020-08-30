#include <bits/stdc++.h>
#include <sys/stat.h>
#include <unistd.h>
using namespace std;
int main()
{
    chdir("/Volumes/Macintosh HD - Data/Logs/");
    ofstream o("August/test.txt");
    if(!o.is_open())
    {
        mkdir("August", 0777);
    }
    o << time(0);
}