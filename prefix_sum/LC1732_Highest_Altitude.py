"""
1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.


Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

Topics
Array
Prefix Sum

Hint 1
Let's note that the altitude of an element is the sum of gains of all the elements behind it
Hint 2
Getting the altitudes can be done by getting the prefix sum array of the given array


Key Developer Insights
The biker starts at altitude 0.
Each gain[i] represents the change from point i to i+1.
We compute a running sum (prefix sum) of gains and track the maximum altitude reached.

Pseudocode (Grounded in Our Principles)

function largest_altitude(gain):
    altitude = 0
    max_altitude = 0

    for delta in gain:
        altitude += delta
        max_altitude = max(max_altitude, altitude)

    return max_altitude

"""

from typing import List, Protocol

class AltitudeStrategy(Protocol):
    def largest_altitude(self, gain: List[int]) -> int: ...

class PrefixSumAltitudeStrategy:
    """
    SRP: Encapsulates prefix sum logic for altitude tracking.
    OCP: Can extend with altitude logging or visualization.
    """
    def largest_altitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0

        for delta in gain:
            altitude += delta
            max_altitude = max(max_altitude, altitude)

        return max_altitude

class Solution:
    """
    High-level interface depending on abstraction (strategy).
    """
    def __init__(self, strategy: AltitudeStrategy = PrefixSumAltitudeStrategy()) -> None:
        self.strategy = strategy
    
    def largestAltitude(self, gain: List[int]) -> int:
        return self.strategy.largest_altitude(gain)


# Usage
solver = Solution()
print(solver.largestAltitude([-5,1,5,0,-7]))        # 1
print(solver.largestAltitude([-4,-3,-2,-1,4,3,2]))  # 0
