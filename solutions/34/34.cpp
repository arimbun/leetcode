#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // Base case #1
        if (nums.size() == 0) {
            vector<int> r(2,-1);
            return r;
        }

        // Base case #2
        if (nums.size() == 1) {
            if (nums[0] == target) {
                vector<int> r(2,0);
                return r;
            } else {
                vector<int> r(2,-1);
                return r;
            }
        }

        // Binary search
        int s = 0;
        int e = nums.size()-1;
        int p = -1;
        while (s <= e) {
            int mid = s + (e-s)/2;
            
            if (nums[mid] == target) {
                p = mid;
                break;
            } else if (nums[s] <= target && target < nums[mid]) {
                e = mid-1;
            } else {
                s = mid+1;
            }
        }

        vector<int> r;
        int a = p, b = p;
        if (p != -1) {
            // Find first index of occurrence
            if (a > 0) {
                while (nums[a-1] == target) {
                    a--;
                    if (a == 0) break;
                }
            }

            // Find last index of occurrence
            if (b < nums.size()-1) {
                while (nums[b+1] == target) {
                    b++;
                    if (b == nums.size()-1) break;
                }
            }
        }

        r.push_back(a);
        r.push_back(b);
        return r;    
    }
};

int main() {
    Solution s;

    int myints[] = {5,7,7,8,8,10};
    vector<int> nums (myints, myints + sizeof(myints) / sizeof(int) );
    vector<int> t;

    t = s.searchRange(nums, 8);
    cout << t[0] << " " << t[1] << endl;

    t = s.searchRange(nums, 6);
    cout << t[0] << " " << t[1] << endl;

    vector<int> u;
    t = s.searchRange(nums, 0);
    cout << t[0] << " " << t[1] << endl;

    int myints2[] = {0,1,2,3,4,4,4};
    vector<int> nums2 (myints2, myints2 + sizeof(myints2) / sizeof(int) );
    t = s.searchRange(nums2, 2);
    cout << t[0] << " " << t[1] << endl;

    int ints3[] = {0,1,1,1,2,2,3,3,4,4,4,4,5,5,6,7,7,8,8};
    vector<int> nums3 (ints3, ints3 + sizeof(ints3) / sizeof(int) );
    t = s.searchRange(nums3, 6);
    cout << t[0] << " " << t[1] << endl;

    int ints4[] = {0,1,1,2,2,2,2,2,2,2,2,2,3,4,4};
    vector<int> nums4 (ints4, ints4 + sizeof(ints4) / sizeof(int) );
    t = s.searchRange(nums4, 3);
    cout << t[0] << " " << t[1] << endl;

    return 0;
}