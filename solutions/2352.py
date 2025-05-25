from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mapz = {}
        for row in range(len(grid)):
            key = ''
            for col in range(len(grid[row])):
                key += str(grid[row][col])

                if col < len(grid[row])-1:
                    key += '-'

            if key not in mapz:
                mapz[key] = [0,0]
            mapz[key] = [mapz[key][0]+1,mapz[key][1]]

        transposed_grid = [list(row) for row in zip(*grid)]
        for row in range(len(transposed_grid)):
            key = ''
            for col in range(len(transposed_grid[row])):
                key += str(transposed_grid[row][col])

                if col < len(transposed_grid[row])-1:
                    key += '-'

            if key not in mapz:
                mapz[key] = [0,0]
            mapz[key] = [mapz[key][0],mapz[key][1]+1]

        result = 0
        for v in mapz.values():
            if v[0] > 0 and v[1] > 0:
                result += v[0]*v[1]

        return result


sol = Solution()
print(sol.equalPairs(grid=[[3,2,1],[1,7,6],[2,7,7]]))
print(sol.equalPairs(grid=[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
