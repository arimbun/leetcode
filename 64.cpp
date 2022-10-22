#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();

        int sums[rows][cols];

        for (int m = 0; m < rows; m++) {
            for (int n = 0; n < cols; n++) {
                int val = grid[m][n];
                if (m == 0) {
                    if (n == 0) sums[m][n] = grid[m][n];
                    else sums[m][n] = sums[m][n-1]+val;
                }
                else {
                    if (n == 0) sums[m][n] = sums[m-1][n]+val;
                    else sums[m][n] = min(sums[m][n-1]+val, sums[m-1][n]+val);
                }
            }
        }
        return sums[rows-1][cols-1];
    }
};

int main() {
    Solution s;

    int arr[] = {{1,3,1},{1,5,1},{4,2,1}};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.minPathSum(nums) << endl;

    int arr2[] = {1, 2};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    cout << s.minPathSum(nums2) << endl;

    return 0;
}
