#include <iostream>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <cstdlib>

using namespace std;

// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

// The solution
class Solution {
public:
    int romanToInt(string s) {
        int x = 0, c = 0;
        int prev = 0;

        for (int i = s.size()-1; i >= 0; i--) {
            switch (s[i]) {
                case 'M':
                    c = 1000;
                    x += c;
                    break;
                case 'D':
                    c = 500;
                    x += c;
                    break;
                case 'C':
                    c = 100;
                    if (prev == 500 || prev == 1000) x -= c;
                    else x += c;
                    break;
                case 'L':
                    c = 50;
                    x += c;
                    break;
                case 'X':
                    c = 10;
                    if (prev == 50 || prev == 100) x -= c;
                    else x += c;
                    break;
                case 'V':
                    c = 5;
                    x += c;
                    break;
                case 'I':
                    c = 1;
                    if (prev == 5 || prev == 10) x--;
                    else x++;
                    break;
                default:
                    break;
            }
            prev = c;
        }

        return x;
    }
};

int main() {
    Solution s;
    cout << s.romanToInt("MXIV") << endl; // 16
    return 0;
}