#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> m;
        m.push_back(1);
        m.push_back(2);

        if (n <= 2) return m[n-1];

        for (int i = 2; i < n; i++) {
            int j = m[i-1] + m[i-2];
            m.push_back(j);
        }
        return m[n-1];
    }
};

int main() {
    Solution s;

    cout << s.climbStairs(5) << endl;

    return 0;
}