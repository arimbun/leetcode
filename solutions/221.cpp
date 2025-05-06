#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <limits>

#define INT_MAX __INT_MAX__

using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();
        int largest = 0;
        int dp[rows][cols];
        for (int m = 0; m < rows; m++) {
            for (int n = 0; n < cols; n++) {
                if (m == 0 || n == 0) {
                    dp[m][n] = (matrix[m][n] == '1') ? 1 : 0;
                } else {
                    if (matrix[m][n] == '1') {
                        if (matrix[m-1][n-1] == '1' && matrix[m-1][n] == '1' && matrix[m][n-1] == '1') {
                            dp[m][n] = min(min(dp[m-1][n], dp[m][n-1]), dp[m-1][n-1]) + 1;
                        } else {
                            dp[m][n] = 1;
                        }
                    } else {
                        dp[m][n] = 0;
                    }
                }
                largest = max(largest, dp[m][n]);
            }
        }

        return largest*largest;
    }
};

int main() {
    Solution s;

    cout << s.maximalSquare(12) << endl;

    return 0;
}
