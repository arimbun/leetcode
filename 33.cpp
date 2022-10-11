#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int s = 0;
        int e = nums.size()-1;
        
        while (s <= e) {
            int mid = s + (e-s)/2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] >= nums[s]) { //means left part is sorted
                if (nums[s] <= target && target < nums[mid]) { 
                    e = mid-1;
                } else {
                    s = mid+1;
                }
            } else {  //means right part is sorted
                if (nums[e] >= target && target > nums[mid]) {
                    s = mid+1;
                } else {
                    e = mid-1;
                }
            }
        }
        
        return -1;
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