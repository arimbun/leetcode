#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (int r = 0; r < matrix.size(); r++) {
            vector<int> row = matrix[r];
            int s = 0;
            int e = row.size()-1;

            // Base cases
            if (target > row[e]) continue;
            if (target < row[s]) return false;

            // Binary search
            if (target <= row[e]) {
                int p = -1;
                while (s <= e) {
                    int mid = s + (e-s)/2;
                    
                    if (row[mid] == target) {
                        return true;
                    } else if (row[s] <= target && target < row[mid]) {
                        e = mid-1;
                    } else {
                        s = mid+1;
                    }
                }
            }
        }        

        return false;
    }
};

int main() {
    Solution s;

    int myints[] = {4,5,6,9,10,11,1,2,3};
    vector<int> nums (myints, myints + sizeof(myints) / sizeof(int) );
    cout << s.search(nums, 2) << endl;
    cout << s.search(nums, 8) << endl;

    return 0;
}