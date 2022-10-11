#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> v;
        v.push_back("()");
        if (n == 1) {
            return v;
        }

        vector<string> r;
        map<int, vector<string> > m;
        for (int i = 2; i <= n; i++) {
            
        }

        return r;
    }
};

int main() {
    Solution s;

    vector<string> v = s.generateParenthesis(1);
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << endl;

    return 0;
}