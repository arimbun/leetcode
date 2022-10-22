#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size(), cols = obstacleGrid[0].size();

        int ways[rows][cols];
        for (int m = 0; m < rows; m++) {
            for (int n = 0; n < cols; n++) {
                if (obstacleGrid[m][n] == 1) {
                    ways[m][n] = 0;
                } else if (m == 0) {
                    if (n == 0) ways[m][n] = 1;
                    else ways[m][n] = ways[m][n-1];
                } else {
                    if (n == 0) ways[m][n] = ways[m-1][n];
                    else {
                        if (obstacleGrid[m][n-1] == 1 && obstacleGrid[m-1][n] == 1) ways[m][n] = 0;
                        else if (obstacleGrid[m][n-1] == 1) ways[m][n] = ways[m-1][n];
                        else if (obstacleGrid[m-1][n] == 1) ways[m][n] = ways[m][n-1];
                        else ways[m][n] = ways[m][n-1]+ways[m-1][n];
                    }
                }
            }
        }
        return ways[rows-1][cols-1];
    }
};

int main() {
    Solution s;

    int arr[] = {{1,3,1},{1,5,1},{4,2,1}};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(int) );
    cout << s.uniquePaths(nums) << endl;

    int arr2[] = {1, 2};
    vector<int> nums2 (arr2, arr2 + sizeof(arr2) / sizeof(int) );
    cout << s.uniquePaths(nums2) << endl;

    return 0;
}
