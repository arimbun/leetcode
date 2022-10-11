#include <iostream>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next() {}
    ListNode(int x) : val(x), next() {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// The solution
class Solution {
public:
    int test() {
        map<int, int> m;
        return m[0];
    }
};

int main() {
    Solution s;
    cout << s.test() << endl;
    
    return 0;
}