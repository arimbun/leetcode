#include <iostream>
#include <stack>
#include <queue>

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
    bool isPalindrome(ListNode* head) {
        stack<int> s;
        queue<int> q;

        while (true) {
            s.push(head->val);
            q.push(head->val);
            if (!(head->next)) break;
            head = head->next;
        }

        int a, b;
        while (!s.empty()) {
            a = s.top(); 
            b = q.front();
            if (a != b) return false;
            s.pop(); 
            q.pop();
        }

        return true;
    }
};

int main() {
    Solution s;

    ListNode aa(1);
    ListNode z(2, &aa);
    ListNode y(2, &z);
    ListNode x(1, &y);

    // cout << x.val << " " << x.next->val << endl;
    if (s.isPalindrome(&x)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
    
    return 0;
}