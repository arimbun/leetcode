from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # X = List [ coordinates[1] ] sorted ascending
        X = set()
        for itv in intervals:
            X.add(itv[0])
        X = sorted(list(X))

        # Y = Map { coordinate[1] : [ list of all intervals ] }
        Y = {}
        for itv in intervals:
            start = itv[0]
            if start not in Y:
                Y[start]=[]
            Y[start].append(itv)

        # declare Z = { coordinate : upper bound }
        Z = {}

        # for each x in X
        #   y = [ list of all intervals ] in Y where coordinate[1] = x
        #   z = ( x, upper bound )
        #   if current_z's x is lower than previous_z's upperbound
        #       update previous z's upper bound value to current_z's upper bound
        #   else
        #       add z as new entry to Result
        z_prev = []
        for x in X:
            y = Y[x]
            ubound = float('-inf')
            for yy in y:
                ubound = max(ubound, yy[1])
            z = [x, ubound]

            if z_prev and x <= z_prev[1]:
                Z[z_prev[0]] = [z_prev[0], max(z_prev[1],ubound)]
                z_prev = [z_prev[0], max(z_prev[1],ubound)]
            else:
                Z[x] = [x, ubound]
                z_prev = [x, ubound]

        result = []
        for _, v in Z.items():
            result.append(v)

        return result

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))
print(sol.merge([[1,4],[2,3]]))
print(sol.merge([[1,4],[0,2],[3,5]]))
