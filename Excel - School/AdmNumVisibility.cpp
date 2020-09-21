#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
    int r = 0, n = 0;
    char c = 0;
    cout << "Enter the master column: ";
    cin >> c;
    cout << "Enter the first row: ";
    cin >> r;
    cout << "Enter the number of students: ";
    cin >> n;
    cout << "Enter the numbers:\n";
    vector<int> rollNum(n);
    for(int i = 0; i < n; i++)
    {
        cin >> rollNum[i];
    }
    ofstream o("output.txt", ofstream::trunc);
    for(int i = 0; i < n; i++)
    {
        o << "=IF(" << c << r + i << " = \"Paid\", " << rollNum[i] << ", )\n";
    }
}