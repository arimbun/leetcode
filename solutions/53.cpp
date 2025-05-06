#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int best_sum = -10000;
        int current_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            current_sum = max(nums[i], current_sum+nums[i]);
            best_sum = max(current_sum, best_sum);
        }

        return best_sum;
    }
};

int main() {
    Solution s;

    int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.maxSubArray(nums) << endl;

    int arr2[] = {-1};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    cout << s.maxSubArray(nums2) << endl;

    int arr3[] = {5,4,-1,7,8};
    vector<int> nums3 (arr3, arr3 + sizeof(arr3) / sizeof(int) );
    cout << s.maxSubArray(nums3) << endl;

    return 0;
}
