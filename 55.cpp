#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool reachable(int curr, vector<int>& nums, vector<int>& m) {
        if (m[curr] == 1) return true;
        else if (m[curr] == 0) return false;

        if (curr == nums.size()-1) {
            // Reached last index (or beyond) - return true
            m[curr] = 1;
            return true;
        }
        
        if (nums[curr] == 0) {
            // Unable to step further - return false
            m[curr] = 0;
            return false;
        }  

        int x = ( nums[curr] < nums.size()-1-curr ) ? nums[curr] : nums.size()-1-curr;
        for (int i = x; i >= 0; i--) {
            if (reachable(curr+i, nums, m)) {
                m[curr] = 1;
                return true;
            } else {
                m[curr] = 0;
            }
        }

        return false;
    }

    bool canJump(vector<int>& nums) {
        vector<int> m(nums.size(), -1);
        if (nums.size() == 1) return true;
        if (nums[0] == 0) return false;
        return reachable(0, nums, m);
    }
};

int main() {
    Solution s;
    int arr[] = {2,3,1,1,4};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    if (s.canJump(nums)) cout << "true" << endl;
    else cout << "false" << endl;

    int arr2[] = {3,2,1,0,4};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    if (s.canJump(nums2)) cout << "true" << endl;
    else cout << "false" << endl;
    return 0;
}