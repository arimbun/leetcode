#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <limits>

#define INT_MAX __INT_MAX__

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> dfs(TreeNode* node) {
        vector<int> q;
        if (node == NULL) {
            return q;
        }

        if (node->left == NULL && node->right == NULL) {
            q.push_back(node->val);
            return q;
        }

        vector<int> ql, qr, qall;
        ql = dfs(node->left);
        qr = dfs(node->right);
        for (int i = 0; i < ql.size(); i++)
            qall.push_back(ql[i]);
        for (int i = 0; i < qr.size(); i++)
            qall.push_back(qr[i]);
        return qall;
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        return dfs(root1) == dfs(root2);
    }
};

int main() {
    return 0;
}
