from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [[]]
        # X = List [ coordinates[1] ] sorted ascending

        # Y = Map { coordinate[1] : [ list of all intervals ] }

        # declare Result = { coordinate : upper bound }
        # for each x in X
        #   y = [ list of all intervals ] in Y where coordinate[1] = x
        #   z = ( x, upper bound )
        #   if current_z's x is lower than previous_z's upperbound
        #       set previous z's uppper bound value to current_z's upper bound
        #   else
        #       add z as new entry to Result

        return result

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))
