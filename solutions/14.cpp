#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string shortest;
        int shortest_len = 9999;
        for (int i = 0; i < strs.size(); i++) {
            if (strs[i].size() < shortest_len) {
                shortest_len = strs[i].size();
                shortest = strs[i];
            }
        }

        string prefix = "";
        for (int i = 0; i < shortest.size(); i++) {
            char c = shortest[i];
            for (int j = 0; j < strs.size(); j++) {
                string str = strs[j];
                char curr_c = str[i];
                if (curr_c != c) return prefix;
            }
            prefix = prefix+c;
        }
        return prefix;
    }
};

int main() {
    Solution s;

    string arr[] = {"flower","flow","flight"};
    vector<string> ss (arr, arr + sizeof(arr) / sizeof(string) );
    cout << s.longestCommonPrefix(ss) << endl;

    return 0;
}
