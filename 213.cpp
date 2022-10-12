#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        vector<int> mem0(nums);
        vector<int> mem1(nums);
        mem0[0] = 0;
        mem1[0] = nums[0];
        mem0[1] = nums[1];
        mem1[1] = mem1[0];
        for (int i = 2; i < nums.size(); i++) {
            mem0[i] = max(mem0[i-1], mem0[i-2]+nums[i]);

            if (i == nums.size()-1) 
                mem1[i] = max(mem1[i-1], mem1[i-2]);
            else 
                mem1[i] = max(mem1[i-1], mem1[i-2]+nums[i]);
        }

        return max(mem0.back(), mem1.back());
    }
};

int main() {
    Solution s;

    int arr[] = {2,1,1,2};
    vector<int> money (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.rob(money) << endl;

    return 0;
}