#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> occ;
        int longest = 0, curr = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (occ[c] == 0) {
                occ[c] = i+1;
                curr++;
                longest = max(longest, curr);
            } else {
                int k = 0;
                longest = max(longest, curr);
                curr = i+1-occ[c];
                k = occ[c]-1; //

                occ.clear();
                for (int j = i; j > k; j--) occ[s[j]] = j+1;

                occ[c] = i+1;
            }
        }
        return longest;
    }
};

int main() {
    Solution s;

    string ss = "abcabcbb";
    cout << s.lengthOfLongestSubstring(ss) << endl;

    string ss1 = "bbbbb";
    cout << s.lengthOfLongestSubstring(ss1) << endl;

    string ss2 = "pwwkew";
    cout << s.lengthOfLongestSubstring(ss2) << endl;

    string ss3 = "tmmzuxt";
    cout << s.lengthOfLongestSubstring(ss3) << endl;

    return 0;
}
