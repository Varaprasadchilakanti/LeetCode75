"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

Topics
Array
Stack
Simulation

Hint 1
Say a row of asteroids is stable. What happens when a new asteroid is added on the right?


Key Developer Insights
Each asteroid moves either right (+) or left (-).
Collisions only occur when:
A positive asteroid (moving right) is followed by a negative asteroid (moving left).

Rules:
If abs(left) > abs(right), the right asteroid explodes.
If abs(left) < abs(right), the left asteroid explodes.
If equal, both explode.

Use a stack to simulate:
Push asteroids moving right.
When a left-moving asteroid comes, check collisions with the stack top until stable.

Pseudocode

function asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:
        alive = True
        while alive and asteroid < 0 and stack and stack[-1] > 0:
            if abs(stack[-1]) < abs(asteroid):
                pop stack[-1]
                continue
            elif abs(stack[-1]) == abs(asteroid):
                pop stack[-1]
            alive = False

        if alive:
            push asteroid onto stack

    return stack

"""

from typing import List, Protocol

class CollisionStrategy(Protocol):
    def asteroid_collision(self, asteroids: List[int]) -> List[int]: ...

class StackCollisionStrategy:
    """
    SRP: Encapsulates stack-based asteroid collision simulation.
    OCP: Can extend with deque or recursive variants.
    """
    def asteroid_collision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                alive = False
            if alive:
                stack.append(asteroid)
        return stack

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: CollisionStrategy = StackCollisionStrategy()) -> None:
        self.strategy = strategy
    
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        return self.strategy.asteroid_collision(asteroids)


# Usage

solver = Solution()
print(solver.asteroidCollision([5,10,-5]))        # [5,10]
print(solver.asteroidCollision([8,-8]))           # []
print(solver.asteroidCollision([10,2,-5]))        # [10]
print(solver.asteroidCollision([3,5,-6,2,-1,4]))  # [-6,2,4]
