from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for roid in asteroids:
            if roid > 0:
                result.append(roid)
            else:
                target = result[-1:]
                if not len(target):
                    # no target
                    result.append(roid)
                elif target[0] < 0:
                    # target will not cause collision
                    result.append(roid)
                else:
                    # target will cause collision!
                    destroyed = False
                    while not destroyed:
                        target = result[-1:]
                        if not len(target):
                            # this roid is stronk!
                            result.append(roid)
                            break
                        elif target[0] < 0:
                            # target will not cause collision
                            result.append(roid)
                            break

                        if abs(roid) < abs(target[0]):
                            destroyed = True
                        elif abs(roid) == abs(target[0]):
                            destroyed = True
                            result = result[:len(result)-1]
                        else:
                            result = result[:len(result)-1]

        return result

s = Solution()
print(s.asteroidCollision(asteroids = [5,10,-5]))
print(s.asteroidCollision(asteroids = [8,-8]))
print(s.asteroidCollision(asteroids = [10,2,-5]))
print(s.asteroidCollision(asteroids = [-2,-2,1,-2]))
