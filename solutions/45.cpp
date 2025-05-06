#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int number_of_jumps(int curr, vector<int>& nums, vector<int>& m, int jumps) {
        if (m[curr] <= jumps) return m[curr];
        m[curr] = jumps;

        // Reached last index
        if (curr == nums.size()-1) {
            return m[curr];
        }

        // Unable to step further
        if (nums[curr] == 0) {
            return m[curr];
        }

        int x = ( nums[curr] < nums.size()-1-curr ) ? nums[curr] : nums.size()-1-curr;
        int y = 0;
        for (int i = x; i > 0; i--) {
            if (m[curr+i] <= jumps+1) continue;
            y = number_of_jumps(curr+i, nums, m, jumps+1);
            m[curr] = min(m[curr], y);
        }

        return m[curr];
    }

    int jump(vector<int>& nums) {
        vector<int> m(nums.size(), 99999);
        if (nums.size() == 1) return 0;
        number_of_jumps(0, nums, m, 0);
        return m[nums.size()-1];
    }
};

int main() {
    Solution s;
    int arr[] = {2,3,1,1,4};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.jump(nums) << endl;

    int arr2[] = {2,3,0,1,4};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    cout << s.jump(nums2) << endl;

    int arr3[] = {5,9,3,2,1,0,2,3,3,1,0,0};
    vector<int> nums3 (arr3, arr3 + sizeof(arr3) / sizeof(int) );
    cout << s.jump(nums3) << endl;

    int arr4[] = {8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5};
    vector<int> nums4 (arr4, arr4 + sizeof(arr4) / sizeof(int) );
    cout << s.jump(nums4) << endl;
    return 0;
}
