from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        a = 0
        b = math.ceil( max(dist) )*101

        speed = int( (a+b)/2 )
        speed_prev = -1
        min_speed = float('inf')
        while speed != speed_prev:
            if speed == 0:
                return min_speed

            total_time = 0
            for i in range(len(dist)):
                time = dist[i]/speed
                if i < len(dist)-1:
                    time = math.ceil(time)
                total_time += time

            if total_time <= hour:
                min_speed = min(speed, min_speed)
                b = speed   # try reducing speed and see if we can go lower
            else:
                a = speed   # too slow! increase speed

            speed_prev = speed
            speed = int( (a+b)/2 )  # reset speed

        # correct min_speed if it equals inf
        if min_speed == float('inf'):
            min_speed = -1
        return min_speed

sol = Solution()
print( sol.minSpeedOnTime(dist = [1,3,2], hour = 6) )       # 1
print( sol.minSpeedOnTime(dist = [1,3,2], hour = 2.7) )     # 3
print( sol.minSpeedOnTime(dist = [1,3,2], hour = 1.9) )     # -1
print( sol.minSpeedOnTime(dist = [1,1,100000], hour = 2.01) )     # 10000000
