#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int highest = prices[0];
        bool decreasing = true;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] > highest) {
                decreasing = false;
                break;
            }
            highest = prices[i];
        }
        if (decreasing) return 0;

        int max_profit = 0, profit = 0, lowest = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            profit = max(profit, prices[i]-lowest);
            max_profit = max(max_profit, profit);
            lowest = min(lowest, prices[i]);
        }

        return profit;
    }
};

int main() {
    Solution s;

    int arr[] = {7,1,5,3,6,4};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.maxProfit(nums) << endl;

    int arr2[] = {7,6,4,3,1};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    cout << s.maxProfit(nums2) << endl;

    int arr3[] = {4,9,1,2};
    vector<int> nums3 (arr3, arr3 + sizeof(arr3) / sizeof(int) );
    cout << s.maxProfit(nums3) << endl;

    return 0;
}
