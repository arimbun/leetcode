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
    int minSetSize(vector<int>& arr) {
        map<int, int> m;
        for (int i = 0; i < arr.size(); i++) {
            m[arr[i]]++;
        }

        priority_queue<int> pq;
        auto iter = m.begin();
        while (iter != m.end()) {
            pq.push(iter->second);
            ++iter;
        }

        int c = 0, t = 0;
        while (t < arr.size()/2) {
            t += pq.top();
            pq.pop();
            c++;
        }

        return c;
    }
};

int main() {
    Solution s;
    // map<int, int> s;
    // s[0]++;
    // cout << s[0] << endl;

    int myints[] = {3,3,3,3,5,5,5,2,2,7};
    vector<int> arr(myints, myints + sizeof(myints) / sizeof(int));
    cout << s.minSetSize(arr) << endl;
    
    return 0;
}