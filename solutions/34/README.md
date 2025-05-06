# Intuition

A naive solution to look for `target` is to iterate through the array. This approach takes $$O(n)$$ time. However, as `nums` is a sorted array we can use binary search to look up `target` efficiently. 

Start with the base cases:

* If `nums.length == 0` then return `[-1,-1]`
* If `nums.length == 1` then `nums[0]` is either equal to the `target` or it is not. If it is equal to the `target` then return `[0,0]` else return `[-1,-1]`

If `nums.length >= 2` then we need to find an occurrence of `target` in the array as quickly as possible. 

# Approach
<!-- Describe your approach to solving the problem. -->

## 1. Searching for the Target (Binary Search Explained)

 Let `s` be the index of `target` in the array if it exists. Since the array allows for duplicate values, there is always the possibility of having more than one `target` in the array, but more on that later.

If we start the search from the tail end of the array (let's call the element at the tail end `last(nums)`), and set a pointer `p = index_of( last(nums) )`then one of these three conditions will be true:

1. `nums[p]` is equal to `target`, OR
2. `nums[p]` is less than `target`, OR
3. `nums[p]` is greater than `target`.

If #1 is true then great, we have found `target`, or at least an occurrence of it (recall that the array may have duplicate values). We can set `s = p` and proceed to **Step 2 - Find First and Last Occurrence of Target** below.

If #2 is true, then we can safely assume that `target` does not exist in the array, hence we return `[-1,-1]`.

If #3 is true, then we should check the elements to the left of `p`. Using binary search, this means the next element we should check is located at position `nums.size()/2` or approximately in the middle of the array. Hence we set our pointer `p = nums.size()/2`. At this point, we again check against the 3 conditions (above):

1. Is `nums[p]` is equal to `target`? OR
2. Is `nums[p]` is greater than `target`?
3. Is `nums[p]` is less than `target`? OR

If #1 is true then great, we have found `target`. If #2 is true then we again perform binary search on the left side of `p`. If #3 is true, then we can now perform binary search on the right side of `p`, since `p` is not the last element of the array. 

We continue with binary search until either:

1. An occurrence of `target` is found, OR
2. Binary search is unable to find `target`, in which case we return `[-1,-1]`

In the case of #1, proceed to **Step 2 - Find First and Last Occurrence of Target**.

## 2. Find First and Last Occurrence of Target 

Once we have found `target`, then `nums[s] == target`. We still need to check elements to the left and right of `s` whether they are equal to `target`. 

Let `a` be equal to the first occurrence of `target` in the array and `b` be equal to the last occurrence of `target` in the array. Initially `a = p` and `b = p`. We continue decrementing `a` until it finds an element that is lower in value than `target` (or it reaches the first element). The element just before that will be the first occurrence of `target`. Similarly, we continue incrementing `b` until it finds an element that is higher in value than `target` (or it reaches the last element). The element just before that will be the last occurrence of `target`.

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(log n)$$ where `n` is the size of the array `nums`.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$ where `n` is the size of the array `nums`.

# Code
```
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
```