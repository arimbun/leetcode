from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # setup days_bin
        #    days_bin[i] = 1 if person is traveling on the i-th day
        #    else days_bin[i] = 0
        days_bin = [0] * 366
        for d in days:
            days_bin[d] = 1

        # build array of min cost
        min_costs = [float('inf')] * 366
        min_costs[0] = 0

        for i in range(1, 366):
            # calculate min cost for the current day
            if days_bin[i] == 0:
                min_costs[i] = min(min_costs[i-1], min_costs[i])
            else:
                c = min(costs[0],costs[1],costs[2]) # buy the cheapest ticket possible
                min_costs[i] = min(min_costs[i-1]+c, min_costs[i])

            # backtrack to check if we would be better with a 30-day pass
            if i >= 7:
                min_costs[i] = min(min_costs[i-7]+costs[1], min_costs[i])

            # backtrack to check if we would be better with a 30-day pass
            if i >= 30:
                min_costs[i] = min(min_costs[i-30]+costs[2], min_costs[i])

        return min_costs[365]


days1 = [1,4,6,7,8,20]
costs1 = [2,7,15]

days2 = [1,2,3,4,5,6,7,8,9,10,30,31]
costs2 = [2,7,15]

days3 = [1,5,8,10,13,20,29,31,37,48,52,53,54,61,63,64,65,67,72,73,74,79,81,84,85,86,87,88,91,94,98,100,108,112,115,116,120,121,123,131,132,135,137,139,141,145,147,152,163,165,166,173,174,178,179,182,187,198,202,203,204,206,208,210,212,213,216,224,230,234,237,239,240,242,247,249,250,257,259,261,263,265,266,272,273,274,275,279,280,281,284,288,292,293,297,298,300,301,304,306,309,318,323,326,328,330,332,335,336,339,341,342,345,350,351,362,365]
costs3 = [15,8,3]

s = Solution()
print(s.mincostTickets(days1, costs1)) # 11
print(s.mincostTickets(days2, costs2)) # 17
print(s.mincostTickets(days3, costs3)) # 39
