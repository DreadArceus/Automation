//Left for later, file system interactions are complicated.
#include <bits/stdc++.h>
#include <sys/stat.h>
#include <unistd.h>
using namespace std;
int main()
{
    const char* baseDir = "/Volumes/Macintosh HD - Data/Logs";
        chdir(baseDir);
    struct stat buf;
    if( stat( baseDir, &buf) != 0 )
    {
        cout << "Unable to access the path";
        //return -1;
    }
    //if( S_ISDIR(buf.st_mode) )
    {
        mkdir("August", 0777);
    }

    ofstream o("test.txt");
    o << time(0);
}