#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0) {
            vector<int> r(2,-1);
            return r;
        }

        if (nums.size() == 1) {
            if (nums[0] == target) {
                vector<int> r(2,0);
                return r;
            } else {
                vector<int> r(2,-1);
                return r;
            }
        }
        
        bool searched[nums.size()];
        for (int i = 0; i < nums.size(); i++) searched[i] = false;

        int i = 0, j = nums.size()-1, k = j/2, s = -1;
        if (nums[j] == target) {
            s = j;
        } else {
            while (!searched[k]) {
                searched[k] = true;
                int x = nums[k];

                if (x == target) {
                    s = k;
                    break;
                } else if (x < target) {
                    i = k;
                    k = (i+j)/2;
                } else {
                    j = k;
                    k = (i+k)/2;
                }
            }
        }

        int a = s, b = s;
        if (a > 0) {
            while (nums[a-1] == target) {
                a--;
                if (a == 0) break;
            }
        }

        if (b < nums.size()-1) {
            while (nums[b+1] == target) {
                b++;
                if (b == nums.size()-1) break;
            }
        }

        vector<int> r;
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