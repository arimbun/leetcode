from typing import List

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        a = 0
        b = max(quantities)*2

        x = int( (a+b)/2 )  # 'x' is the number of packages
        x_prev = -1
        x_min = float('inf')
        while x_prev != x:
            if x == 0:
                return x_min

            curr_n = 0
            for qt in quantities:
                curr_n += int(qt/x)
                if qt%x > 0:
                    curr_n+=1

            if curr_n <= n:
                if x < x_min:
                    x_min = x
                # some shops don't get packages - try reducing x
                b = x
            else:
                # too many shops - try increasing x
                a = x

            x_prev = x
            x = int( (a+b)/2 )
        return x_min

sol = Solution()
print(sol.minimizedMaximum(n = 6, quantities = [11,6])) # 3
print(sol.minimizedMaximum(n = 7, quantities = [15,10,10])) # 5
print(sol.minimizedMaximum(n = 1, quantities = [1])) # 1
print(sol.minimizedMaximum(n = 19, quantities = [26,1,11,7,8,5,18,16,7,21,1,10,30,30])) # 16
