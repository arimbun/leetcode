#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> a, b;
        for (int i = 0; i < ransomNote.length(); i++) {
            a[ransomNote[i]] += 1;
        }

        for (int i = 0; i < magazine.length(); i++) {
            b[magazine[i]] += 1;
        }

        auto iter = a.begin();
        while (iter != a.end()) {
            if (b[iter->first] < iter->second) {
                return false;
            }
            ++iter;
        }
        
        return true;
    }
};

int main() {
    Solution s;
    cout << s.canConstruct("aab", "aabc") << endl;
    return 0;
}