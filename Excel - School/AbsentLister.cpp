#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{
    int n = 0;
    cout << "enter the number of students: ";
    cin >> n;
    cout << "enter the attendance matrix:\n";
    vector<vector<int>> days(31);
    for(int i = 0; i < n; i++)
    {
        int currentRoll = 0;
        cin >> currentRoll;
        string s = "";
        getline(cin, s);
        int x = 1;
        for(int j = 0; j < 31; j++)
        {
            if(x + 2 < s.length() && s[x] == 'A' && s[x+2] == 'A')
            {
                days[j].push_back(currentRoll);
            }
            x += 4;
        }
    }
    cout << "\nResult:\n";
    for(int i = 0; i < 31; i++)
    {
        for(int j = 0; j < days[i].size(); j++)
        {
            cout << days[i][j] << " ";
        }
        cout << "\n";
    } 
}