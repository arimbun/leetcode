#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        string t = s;
        reverse(t.begin(), t.end());
        if (s == t) return s;

        bool pal[s.size()][s.size()+1];
        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j < s.size()+1; j++) {
                pal[i][j] = false;
            }
        }

        string r, ss;
        int longest = 0;
        // i = start index, j = length of substring
        for (int j = 1; j <= s.size(); j++) {
            if (j > longest+2) break;
            for (int i = 0; i <= s.size()-j; i++) {
                ss = s.substr(i, j);
            
                if (j == 1) {
                    pal[i][j] = true;
                    r = ss;
                    longest = j;
                } else if (j == 2) {
                    if (ss[0] == ss[1]) {
                        pal[i][j] = true;
                        r = ss;
                        longest = j;
                    }
                } else {
                    if (ss[0] == ss[j-1] && pal[i+1][j-2]) {
                        pal[i][j] = true;
                        r = ss;
                        longest = j;
                    } 
                }
            }
        }   

        return r;
    }
};

int main() {
    Solution s;
    cout << s.longestPalindrome("a") << endl;
    cout << s.longestPalindrome("cb") << endl;
    cout << s.longestPalindrome("cc") << endl;
    cout << s.longestPalindrome("cbbadadabx") << endl;
    cout << s.longestPalindrome("abaabab") << endl;
    cout << s.longestPalindrome("babaabab") << endl;
    cout << s.longestPalindrome("aacabdkacaa") << endl;

    return 0;
}