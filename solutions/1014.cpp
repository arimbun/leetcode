#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int max_score = 0, max_left = values[0];
        for (int i = 1; i < values.size(); i++) {
            max_score = max(max_score, max_left+values[i]-i);
            max_left = max(max_left, values[i]+i);
        }
        return max_score;
    }
};

int main() {
    Solution s;

    int arr[] = {8,1,5,2,6};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.maxScoreSightseeingPair(nums) << endl;

    int arr2[] = {1, 2};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    cout << s.maxScoreSightseeingPair(nums2) << endl;

    return 0;
}
