#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        vector<int> mem(nums);
        mem[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size(); i++) {
            mem[i] = max(mem[i-1], mem[i-2]+nums[i]);
        }

        return mem.back();
    }
};

int main() {
    Solution s;

    int arr[] = {0,1,2,3,4,4,4};
    vector<int> money (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.rob(money) << endl;

    return 0;
}